from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.meetingClass      import *
from app.scrum.elementMeetingClass   import *
from app.scrum.backLog           import *
from app.scrum.subEquipoClass           import *
from datetime import datetime

sprint = Blueprint('sprint', __name__)

@sprint.route('/sprint/AActualizarEquipoSprint', methods=['POST'])
def AActualizarEquipoSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEquipoSprint', 'msg':['Sub Equipo actualizado']}, {'label':'/VEquipoSprint', 'msg':['Error al actualizar el Sub equipo']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idSprint  = int(session['idSprint'])
    idPila  = int(session['idPila'])
    obTeam = team()
    idEquipo = obTeam.getTeamId(idPila)

    lista = params['lista']    
    oTeam = subEquipoClass()
    exito = oTeam.actualizar(lista,idSprint)
    if exito:
        res = results[0]
    res['label'] = res['label'] + '/' + repr(1)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/VEquipoSprint')
def VEquipoSprint():
    #GET parameter
    idSprint = int(session['idSprint'])
    idPila  = int(session['idPila'])
    res = {}
    #Action code goes here, res should be a JSON structure
    if "actor" in session:
        res['actor']=session['actor']
   # #Action code goes here, res should be a JSON structure
    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
   
    obTeam = team()
    teamList = obTeam.getTeamDevs(idPila)
    oTeam = subEquipoClass()
    SubteamList = oTeam.getSubEquipo(idSprint)

    res['fEquipo'] = {'lista':[{'miembro':team.SEQ_username, 'rol': team.SEQ_rol} for team in SubteamList]}
    res['usuario'] = session['usuario']
    res['idSprint'] = idSprint

    res['fEquipo_opcionesRol'] =[
        {'key':'Desarrollador', 'value':'Desarrollador'}
      ]

    res['fEquipo_opcionesMiembros'] =[{'key':user.EQ_username,'value': user.EQ_username} for user in teamList]

    #Action code ends here
    return json.dumps(res)




@sprint.route('/sprint/ACrearElementoMeeting', methods=['POST'])
def ACrearElementoMeeting():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VReunion', 'msg':['Elemento de la reunión creado']}, {'label':'/VCrearElementoMeeting', 'msg':['Error al crear un elemento a la reunión']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    idReunion = 1
    res['label'] = res['label'] + '/' + str(idReunion)
    # ATENCION: lo que estas a punto de leer es un cable que debe ser eliminado
    # Por qué es un cable? El query no debería hacerse aquí.
    res['usuario'] = session['usuario']
    usuario = clsUser.query.filter_by(U_fullname = session['usuario']['nombre']).all()[0].U_username
    # fin del cable
    #usuario = 'gennysanchez11'
    challenges = params['challenge']
    planed = params['planed']
    done = params['done']
    #idReunion = int(session['idReunion'])
    oElementMeeting = elementMeeting()
    exito = oElementMeeting.insertElement(challenges, planed, done, idReunion, usuario)
    if exito:
        res = results[0]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



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
    #tipo = params['Tipo'] #NUEVO ATRIBUTO OJO!!! AGREGAR A LA LLAMADA DE LA FUNCION DE ABAJO
    retos = params['Retos']
    tipo = "Presencial"


    oMeeting = meeting()
    exito = oMeeting.insertMeeting(fecha,actividades,sugerencias,retos,tipo,idSprint) #AGREGAR NUEVO ATRIBUTO
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

        # Creamos el subEquipo
        # Obtengo Todos los desarrolladores del Equipo
        oTeam      = team()
        teamList = oTeam.getTeamDevs(idPila)
        oSubTeam = subEquipoClass()
        idSprint = oSprint.getSprintId(newNumero,idPila)
        print('SPRINT ID:::::::::::::: ' + str(idSprint))

        for member in teamList:
            oSubTeam.insertMiembroSubEquipo(member.EQ_username,member.EQ_rol,idSprint)

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


@sprint.route('/sprint/AModifElementoMeeting', methods=['POST'])
def AModifElementoMeeting():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VReunion', 'msg':['Elemento Modificado con exito']},{'label':'/VReunion', 'msg':['Error al modificar elemento']} ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    # Cableada para la presentación. Sólo funciona para modificar los 
    # elementos creados por el usuario de turno en la reunión 1
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    challenges = params['challenge']
    planed = params['planed']
    done = params['done']
    # ATENCIÓN: lo que estás a punto de leer es un cable, pues hay un bug en el que
    # session['idReunion'] arrpja KEY ERROR.
    idReunion = 1
    # ATENCION: lo que estas a punto de leer es un cable que debe ser eliminado
    # Por qué es un cable? El query no debería hacerse aquí.
    res['usuario'] = session['usuario']
    usuario = clsUser.query.filter_by(U_fullname = session['usuario']['nombre']).all()[0].U_username
    # fin del cable
    oElementMeeting = elementMeeting()
    anElement = oElementMeeting.getElementsByUserAndMeeting(usuario, idReunion)[0]
    exito = oElementMeeting.updateElement(anElement.EM_idElementMeeting, challenges, planed, done, idReunion, usuario)
    if exito:
        res = results[0]
    res['label'] = res['label'] + '/' + str(idReunion)

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
    #fecha = params['Fecha']
    actividades = params['Actividades']
    sugerencias = params['Sugerencias']
    retos = params['Retos']
    tipo = params['Tipo'] #NUEVO ATRIBUTO OJO!!! AGREGAR A LA LLAMADA DE LA FUNCION DE ABAJO (updateMeeting)

    oMeeting = meeting()
    result = oMeeting.getMeetingID(idReunion,idSprint)

    exito = oMeeting.updateMeeting(result[0].SM_meetingDate,result[0].SM_meetingDate,actividades,sugerencias,retos,tipo,idSprint)

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



@sprint.route('/sprint/VCrearElementoMeeting')
def VCrearElementoMeeting():
    #GET parameter
    idReunion = request.args['idReunion']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    # ATENCIÓN: lo que estás a punto de leer es un cable, pues hay un bug en el que
    # idReunion tiene valor UNDEFINED
    res['idReunion'] = 1
    res['idSprint'] = 1
    #FIN DEL CABLE

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VCrearReunionSprint')
def VCrearReunionSprint():
    #GET parameter
    res = {}

    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']
    res['idPila']  = idPila
    res['idSprint'] = session['idSprint']
    
    res['fReunion_OpcionesTipo'] =[
        {'key':1, 'value':'Presencial'},
        {'key':2, 'value':'No Presencial'},
    ]


    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VCrearSprint')
def VCrearSprint():
   #GET parameter
    res = {}

    idPila = int(request.args.get('idPila',1))
        
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['fSprint'] = {'idPila':idPila}
    res['usuario'] = session['usuario']
    res['idPila']  = idPila

    return json.dumps(res)




@sprint.route('/sprint/VElementoMeeting')
def VElementoMeeting():
    #GET parameter
    idReunion = int(request.args['idReunion'])
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    # ATENCION: lo que estas a punto de leer es un cable que debe ser eliminado
    # Por qué es un cable? Porque debería ser el username que lo creó y no el que
    # está en sesión. Además, el query no debería hacerse aquí.
    res['usuario'] = session['usuario']
    u = clsUser.query.filter_by(U_fullname = session['usuario']['nombre']).all()[0].U_username
    # fin del cable
    oElementMeeting = elementMeeting()
    anElement = oElementMeeting.getElementsByUserAndMeeting(u, idReunion)[0]
    res['fElementoMeeting'] = {
        'challenge' : anElement.EM_challenges,
        'planed' : anElement.EM_planned,
        'done' : anElement.EM_done,
#      'challenge' :'Carrera inicial. Modelo de datos, MVC, identificación',
#      'planed':'planificado',
#      'done':'realizado',
#      'idReunion':1,
#      'idUser':1,
      }
    res['idElementMeeting'] = anElement.EM_idElementMeeting 
    res['idElemento'] = 1 # Qué es esto?
    res['idReunion'] =  idReunion
    res['idSprint'] = 1

    #Action code ends here
    return json.dumps(res)


@sprint.route('/sprint/VEquipoSprint')



@sprint.route('/sprint/VReunion')
def VReunion():
    #GET parameter
    idReunion = int(request.args.get('id', 1))

    idSprint = session['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    oMeeting = meeting()
    result  = oMeeting.getMeetingID(idReunion,idSprint)

    oElementMeeting = elementMeeting()
    elements  = oElementMeeting.getElements(idReunion)
    res['data4'] = [{'id': e.EM_idElementMeeting, 'user': e.EM_user} for e in elements]

    res['fReunion'] = {'idReunion':idReunion,'idSprint':idSprint, 'Actividades':result[0].SM_activities, 'Sugerencias':result[0].SM_suggestions,'Retos':result[0].SM_challenges, 'Tipo':result[0].SM_typeMeeting}

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
    res['data4'] = [{'id':res.SM_idSprintMeeting, 'fecha':res.SM_meetingDate, 'actividades':res.SM_activities,'tipo':res.SM_typeMeeting } for res in result]  

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

