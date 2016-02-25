# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.backLog           import *

sprint = Blueprint('sprint', __name__)

@sprint.route('/sprint/ACrearSprint', methods=['POST'])
def ACrearSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint creado']}, {'label':'/VSprint', 'msg':['Error al crear Sprint']}, ]
    print(session, file=sys.stderr)
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    
    # Obtenemos el id del producto
    idPila  = int(session['idPila'])

    if request.method == 'POST':
        # Extraemos los parámetros
        newNumero       = params['numero'] 
        newDescription  = params['descripcion']
        
        oSprint = sprints()
        result  = oSprint.insertSprint(newNumero, newDescription, idPila)

        if result:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AElimSprint')
def AElimSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint eliminado']}, {'label':'/VSprint', 'msg':['Error al eliminar Sptrint']}, ]
    res = results[1]
    
    # Obtenemos el id del producto
    idPila       = int(session['idPila'])

    # Obtenemos el id del sprint
    #idSprint = int(params['idSprint'])
    idSprint = int(session['idSprint'])

    # Conseguimos el sprint a eliminar
    oSprint  = sprint()
    found    = oSprint.searchIdSprint(idSprint,idPila)

    if (found != []):
        deleted = oSprint.deleteSprint(found[0].S_numero, found[0].S_idBacklog)

    if deleted:
            res = results[0]  

    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AModifSprint', methods=['POST'])
def AModifSprint():
    #POST/PUT parameters
    params = request.get_json()

    results = [{'label':'/VSprints', 'msg':['Sprint modificado']}, {'label':'/VSprints', 'msg':['Error al guardar Sprint']}, ]
    res = results[0]

    idPila = int(session['idPila'])
    idSprint = int(params['idSprint'])
    newSprintNumber = int(params['numero'])
    newDescription = str(params['descripcion'])

    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + repr(1)
    print(idSprint, idPila, file = sys.stderr )
    oSprint = sprints()
    result = oSprint.updateSprint(idSprint, idPila, newSprintNumber, newDescription)
    if not result:
        res = results[1]        
        res['label'] = res['label'] + '/' + repr(1)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)



@sprint.route('/sprint/VCrearSprint')
def VCrearSprint():
    #GET parameter

    #idPila = request.args['idPila']
    idPila = request.args.get('idPila',1)

    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    res['fSprint'] = {'idPila':idPila}

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprint')
def VSprint():
    #GET parameter

    res = {}

    # Obtenemos el id del producto y del sprint
    idPila  = int(session['idPila'])
    idSprint = int(request.args['idSprint'])
    

    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # res['fSprint'] = {
    #   'idPila':1,
    #   'numero':1, 
    #   'descripcion' :'Carrera inicial. Modelo de datos, MVC, identificación'
    #   }
    # res['idPila'] = 1



    # Buscamos el actor actual
    oSprint = sprints()
    result = oSprint.searchIdSprint(idSprint,idPila)
    print(idSprint)
    res['fSprint'] = {'idSprint':idSprint, 'numero':result[0].S_numero, 'descripcion':result[0].S_sprintDescription}    

    res['idPila'] = idPila
    session['idSprint'] = idSprint

    #Action code ends here
    return json.dumps(res)
    

@sprint.route('/sprint/VSprints')
def VSprints():
    #GET parameter

    idPila = int(request.args.get('idPila',1))

    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']
    res['idPila'] = idPila

    oBacklog   = backlog()
    sprintList = oBacklog.sprintsAsociatedToProduct(idPila)
    res['data1'] = [{'numero':spr.S_numero, 'descripcion':spr.S_sprintDescription } for spr in sprintList]

    return json.dumps(res)





#Use case code starts here


#Use case code ends here

