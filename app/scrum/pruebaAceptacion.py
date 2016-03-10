# -*- coding: utf-8 -*-
from acceptanceTest import *
from flask import request, session, Blueprint, json
import os

pruebaAceptacion = Blueprint('pruebaAceptacion', __name__)

# Where files are going to be uploaded
app.config['UPLOADED_SCRIPT_DEST'] = 'uploadedScripts/'

@pruebaAceptacion.route('/pruebaAceptacion/ACrearPruebaAceptacion', methods=['POST'])
def ACrearPruebaAceptacion():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Prueba creada']}, 
               {'label':'/VHistoria', 'msg':['No se pudo crear la prueba.']}, ]
    res     = results[0]
    
    # Obtenemos el id de la historia actual
    idHistory = int(session['idHistoria'])

    # Extraemos los parámetros
    description = request.form['descripcion']
    file = request.files['contenido']

    file.save(os.path.join(app.config['UPLOADED_SCRIPT_DEST'], file.filename))
    url = str(app.config['UPLOADED_SCRIPT_DEST'] + file.filename)
    oTest = acceptanceTest()
    oTest.insertAcceptanceTest(idHistory,description,url)

    res['label'] = res['label'] + '/' + str(idHistory)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@pruebaAceptacion.route('/pruebaAceptacion/AElimPruebaAceptacion/<idPrueba>')
def AElimPruebaAceptacion(idPrueba):
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Prueba borrada']}, 
               {'label':'/VHistoria', 'msg':['No se pudo eliminar la prueba']}, ]
    res     = results[0]

    # Obtenemos los parámetros

    oPrueba = acceptanceTest()
    print(idPrueba)
    result  = oPrueba.findIdAcceptanceTest(int(idPrueba))

    # Delete physical file
    os.remove(result.AT_urlScript)

    # Eliminamos la prueba
    delete  = oPrueba.deleteAcceptanceTest(result.AT_idAT)

    if delete:
        res = results[0]

    res['label'] = res['label'] + '/' + str(session['idHistoria'])

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@pruebaAceptacion.route('/pruebaAceptacion/VCrearPruebaAceptacion')
def VCrearPruebaAceptacion():
    #GET parameter
    res = {}    
    # Obtenemos el id de la historia actual
    idHistory = int(request.args.get('idHistoria'))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    
    res['usuario']        = session['usuario']

    session['idHistoria'] = idHistory
    res['idHistoria']     = idHistory

    return json.dumps(res)