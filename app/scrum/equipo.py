from flask import request, session, Blueprint, json

equipo = Blueprint('equipo', __name__)


@equipo.route('/equipo/AActualizarEquipo', methods=['POST'])
def AActualizarEquipo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEquipo', 'msg':['Equipo actualizado']}, {'label':'/VEquipo', 'msg':['Error al actualizar el equipo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    print(params['lista'])
    res['label'] = res['label'] + '/' + repr(1)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@equipo.route('/equipo/VEquipo')
def VEquipo():
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
    res['idPila'] = 1
    res['fEquipo'] = {'lista':[
        {'miembro':1, 'rol':1},
        {'miembro':2, 'rol':2},
        {'miembro':3, 'rol':3},
      ]}
    res['fEquipo_opcionesRol'] =[
        {'key':1, 'value':'Desarrollador'},
        {'key':2, 'value':'Scrum master'},
        {'key':3, 'value':'Product owner'},
      ]
    res['fEquipo_opcionesMiembros'] =[
        {'key':1, 'value':'Mia'},
        {'key':2, 'value':'Mara'},
        {'key':3, 'value':'Marcos'},
        {'key':4, 'value':'Julia'},
        {'key':5, 'value':'Roberto'},
      ]
    

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

