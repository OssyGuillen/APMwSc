# -*- coding: utf-8 -*-

from flask                       import request, session, Blueprint, json
from app.scrum.accions           import *
from app.scrum.backLog           import *
from app.scrum.actorsUserHistory import *
from app.scrum.userHistory       import *

accion = Blueprint('accion', __name__)


@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters.
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res     = results[1]

    # Obtenemos el id del producto
    idPila  = int(session['idPila'])


    if params != {}:
        # Extraemos los parámetros
        newDescription = params['descripcion']

        if request.method == 'POST':
            oAccion  = accions()
            inserted = oAccion.insertAccion(newDescription,idPila)

            if inserted:
                res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)



@accion.route('/accion/AElimAccion')
def AElimAccion():
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Accion eliminada']}, {'label':'/VProducto', 'msg':['No se pudo eliminar esta acción']}, ]
    res     = results[1]

    # Obtenemos el id del producto y de la acción
    idPila   = int(session['idPila'])
    idAccion = int(session['idAccion'])

    # Conseguimos la acción a eliminar
    oAccion = accions()
    found   = oAccion.searchIdAccion(idAccion)

    oAccionUserHist = userHistory()
    result  = oAccionUserHist.searchidUserHistoryIdAccion(idAccion)

    # Verificamos si la acción está asociado a una historia
    if (result == []):
        deleted = oAccion.deleteAccion(found[0].AC_accionDescription, idPila)

        if deleted:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VProducto', 'msg':['Error al modificar acción']}, ]
    res     = results[1]

    # Obtenemos el id del producto
    idPila  = int(session['idPila'])

    # Extraemos los parámetros
    newDescription = params['descripcion']
    idAccion       = int(params['idAccion'])

    oAccion = accions()
    found   = oAccion.searchIdAccion(idAccion)
    result  = oAccion.updateAccion(found[0].AC_accionDescription, newDescription,idPila)

    if result:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)



@accion.route('/accion/VAccion')
def VAccion():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y de la acción
    idPila   = int(session['idPila'])
    idAccion = int(request.args.get('idAccion'))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Buscamos la accion actual.
    oAccion = accions()
    result  =  oAccion.searchIdAccion(idAccion)

    res['fAccion'] = {'idAccion':idAccion, 'descripcion':result[0].AC_accionDescription}
    res['idPila']  = idPila
    session['idAccion'] = idAccion

    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    #GET parameter
    res = {}

    # Obtenemos el id del producto
    idPila = request.args.get('idPila',1)

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    res['idPila'] = idPila

    return json.dumps(res)



#Use case code starts here


#Use case code ends here
