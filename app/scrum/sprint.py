from flask import request, session, Blueprint, json

sprint = Blueprint('sprint', __name__)


@sprint.route('/sprint/ACrearSprint', methods=['POST'])
def ACrearSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint creado']}, {'label':'/VSprint', 'msg':['Error al crear Sprint']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    # Obtenemos el id del producto
    idPila  = int(session['idPila'])
    
    if request.method == 'POST':
    
        # Extraemos los parámetros
        newDescription      = params['descripcion']
        
        oSprint = sprint()
        result  = oSprint.insertSprint(newDescription, idPila)

        if result:
            res = results[0]

    res['label'] = res['label'] + '/' + repr(1)

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



@sprint.route('/sprint/AModifSprint', methods=['POST'])
def AModifSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint modificado']}, {'label':'/VSprint', 'msg':['Error al guardar Spront']}, ]
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
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['fSprint'] = {'idPila':1}


    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprint')
def VSprint():
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
    res['fSprint'] = {
      'idPila':1,
      'numero':1, 
      'descripcion' :'Carrera inicial. Modelo de datos, MVC, identificación'
      }
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprints')
def VSprints():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['data1'] = [{'numero':1, 'descripcion':'Carrera inicial'}]
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

