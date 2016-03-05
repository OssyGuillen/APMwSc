from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.meetingClass      import *
from app.scrum.backLog           import *
from datetime import datetime

sprint = Blueprint('sprint', __name__)


@sprint.route('/sprint/ACrearReunionSprint', methods=['POST'])
def ACrearReunionSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Reunion creada']}, {'label':'/VCrearReunionSprint', 'msg':['Error creando reunion']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idPila  = int(session['idPila'])
    idSprint = int(session['idSprint'])
    fecha = params['Fecha']
    actividades = params['Actividades']
    sugerencias = params['Sugerencias']
    retos = params['Retos']

    oMeeting = meeting()
    print ('IDSPRINT', idSprint)
    exito = oMeeting.insertMeeting(fecha,actividades,sugerencias,retos,idSprint)
    print(exito)
    print(fecha)
    if exito:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


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



@sprint.route('/sprint/AModifReunionSprint', methods=['POST'])
def AModifReunionSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VReunion', 'msg':['Reunión de sprint modificada'], "actor":"desarrollador"}, {'label':'/VReunion', 'msg':['Error al modificar reunión'], "actor":"desarrollador"}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idPila  = int(session['idPila'])
    idReunion  = params['idReunion']
    idSprint = int(session['idSprint'])
    fecha = params['Fecha']
    actividades = params['Actividades']
    sugerencias = params['Sugerencias']
    retos = params['Retos']

    oMeeting = meeting()
    result = oMeeting.getMeetingID(idReunion,idSprint)

    exito = oMeeting.updateMeeting(result[0].SM_meetingDate,result[0].SM_meetingDate,actividades,sugerencias,retos,idSprint)

    if exito:
        res = results[0]

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    idSprint = 1
    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    res['idSprint'] = idSprint
    session['idReunion'] = idReunion

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



@sprint.route('/sprint/VCrearReunionSprint')
def VCrearReunionSprint():
    #GET parameter
    res = {}

    idPila = request.args.get('idPila',1)

    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']
    res['idPila']  = idPila
    res['idSprint'] = session['idSprint']

    #Action code ends here
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



@sprint.route('/sprint/VReunion')
def VReunion():
    #GET parameter
    idReunion = request.args['idReunion']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    idSprint = session['idSprint']

    oMeeting = meeting()
    result  = oMeeting.getMeetingID(idReunion,idSprint)

    res['fReunion'] = {'idReunion':idReunion,'idSprint':idSprint, 'Fecha':result[0].SM_meetingDate, 'Actividades':result[0].SM_activities, 'Sugerencias':result[0].SM_suggestions,'Retos':result[0].SM_challenges}

    #Action code ends here
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
    #print (result)
    res['fSprint'] = {'idSprint':idSprint, 'numero':result[0].S_numero, 'descripcion':result[0].S_sprintDescription} 

    oMeeting = meeting()
    result  = oMeeting.getMeetings(idSprint)
    res['data4'] = [{'id':res.SM_idSprintMeeting, 'fecha':res.SM_meetingDate, 'actividades':res.SM_activities } for res in result]  

    session['idSprint'] = idSprint
    res['idSprint'] = idSprint

    session['idPila'] = idPila
    res['idPila'] = idPila

    

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

