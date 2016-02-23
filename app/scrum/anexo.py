from flask import request, session, Blueprint, json

anexo = Blueprint('anexo', __name__)


@anexo.route('/anexo/AAnexo', methods=['POST'])
def AAnexo():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VAnexo', 'msg':['Documento anexado']}, {'label':'/VAnexo', 'msg':['Error al guardar anexo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    print('Nombre del anexo:'+request.form['nombre'])
    res['label'] = res['label'] + '/' + repr(1)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@anexo.route('/anexo/AElimAnexo')
def AElimAnexo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VAnexo', 'msg':['Anexo eliminado']}, {'label':'/VAnexo', 'msg':['Error al eliminar anexo']}, ]
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



@anexo.route('/anexo/VAnexo')
def VAnexo():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['data1'] = [
      {'idAnexo':1, 'nombre':'Diagrama de clases', 'contenido':'diagrama.pdf'},
      {'idAnexo':2, 'nombre':'Diagrama de seccuencia', 'contenido':'diagrama2.pdf'}]
    res['fAnexo'] = {}
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

