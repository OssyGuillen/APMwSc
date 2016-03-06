# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.backLog           import *

sprint = Blueprint('sprint', __name__)

@sprint.route('/sprint/ACrearSprint', methods=['POST'])
def ACrearSprint():
    #POST/PUT parameters
    params   = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint creado']}, {'label':'/VCrearSprint', 'msg':['Error al crear Sprint']}, ]
    res     = results[1]

    # Obtenemos el id del producto
    idPila  = int(session['idPila'])

    if request.method == 'POST':
        # Extraemos los parámetros
        newNumero      = params['numero'] 
        newDescription = params['descripcion']
        
        oSprint = sprints()
        result  = oSprint.insertSprint(newNumero, newDescription, idPila)

        if result:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AElimSprint')
def AElimSprint():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint eliminado']}, {'label':'/VSprint', 'msg':['Error al eliminar Sptrint']}, ]
    res     = results[1]
    
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

    res['label'] = res['label'] + '/' + str(idSprint)

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

    idPila   = int(session['idPila'])
    idSprint = int(session['idSprint'])
    newSprintNumber = int(params['numero'])
    newDescription  = str(params['descripcion'])

    res['label'] = res['label'] + '/' + str(idPila)
    oSprint = sprints()
    result  = oSprint.updateSprint(idSprint, idPila, newSprintNumber, newDescription)
    
    if not result:
        res = results[1]        
        res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    res['idPila'] = idPila


    return json.dumps(res)

@sprint.route('/sprint/ASprintHistoria', methods=['POST'])
def ASprintHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Historia Asignado']}, {'label':'/VSprint', 'msg':['Error al Asignar Historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + repr(1)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/ASprintTarea', methods=['POST'])
def ASprintTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Tarea asignada']}, {'label':'/VSprint', 'msg':['Error al asignar tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

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
    res = {}

    idPila = request.args.get('idPila',1)
        
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['fSprint'] = {'idPila':idPila}
    res['usuario'] = session['usuario']
    res['idPila']  = idPila

    return json.dumps(res)



@sprint.route('/sprint/VSprint')
def VSprint():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y del sprint
    idPila   = int(session['idPila'])
    idSprint = int(request.args.get('idSprint',1))
    
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Buscamos el actor actual
    oSprint = sprints()
    result  = oSprint.searchIdSprint(idSprint,idPila)
    
    res['fSprint'] = {'idSprint':idSprint, 'numero':result[0].S_numero, 'descripcion':result[0].S_sprintDescription}    

    res['data5'] = [
        {'idHistoria':1,'prioridad':'Alta', 'enunciado':'En tanto que cocinero puedo preparar una ratatuya para cenar'},
        {'idHistoria':2,'prioridad':'Media', 'enunciado':'En tanto que chef puedo hacer que los cocineros prepraren varios platos para cumplir con el munú'}
    ]
    res['data7'] = [
      {'idTarea':1, 'descripcion':'Sacarle jugo a una piedra'},
      {'idTarea':2, 'descripcion':'Pelar un mango'},
    ]

    res['idSprint'] = idSprint
    res['idPila'] = idPila


    return json.dumps(res)



@sprint.route('/sprint/VSprintHistoria')
def VSprintHistoria():
    #GET parameter
    idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']
    res['fSprintHistoria_opcionesHistoria'] = [
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]

    res['idPila'] = 1
    res['idSprint']= idSprint

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprintTarea')
def VSprintTarea():
    #GET parameter
    idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']
    res['fSprintTarea_opcionesTarea'] = [
      {'key':1,'value':'Tarea1'},
      {'key':2,'value':'Tarea2'},
      {'key':3,'value':'Tarea3'}]

    res['idPila'] = 1
    res['idSprint']= idSprint

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprints')
def VSprints():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto.
    idPila = int(request.args.get('idPila',1)) 

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']

    oBacklog   = backlog()
    sprintList = oBacklog.sprintsAsociatedToProduct(idPila)
    res['data1'] = [{'numero':spr.S_numero, 'descripcion':spr.S_sprintDescription } for spr in sprintList]


    session['idPila'] = idPila
    res['idPila']     = idPila 
 
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

