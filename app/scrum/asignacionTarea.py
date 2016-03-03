from flask import request, session, Blueprint, json
from task import *

asignacionTarea = Blueprint('asignacionTarea', __name__)


@asignacionTarea.route('/asignacionTarea/AActuralizarAsignacionTarea/<path:idGrupo>', methods=['POST'])
def AActuralizarAsignacionTarea(idGrupo):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VTarea', 'msg':['Asignación actualizada']}, {'label':'/VTarea', 'msg':['Error al actualizar la asignacion de la tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    idTarea  = int(session['idTarea'])
    res['label'] = res['label'] + '/' + str(idTarea)

    c = task()
    c.insertUserTask(idTarea, idGrupo)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@asignacionTarea.route('/asignacionTarea/VAsignacionTarea')
def VAsignacionTarea():
    #GET parameter
    idTarea = request.args['idTarea']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    # temporal harcoding of response
    res['usuario'] = session['usuario']
    res['idPila'] = session['idPila']
    res['idTarea'] = session['idTarea']
    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

