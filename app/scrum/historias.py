from flask import request, session, Blueprint, json

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label']+'/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #Datos de prueba
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AElimHistoria')
def AElimHistoria():
    #GET parameter
    idHistoria = request.args['idHistoria']
    results = [{'label':'/VHistorias', 'msg':['Historia eliminada']}, {'label':'/VHistoria', 'msg':['No se pudo eliminar esta historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #Datos de prueba
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/APrelaciones', methods=['POST'])
def APrelaciones():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrelaciones', 'msg':['Cambios almacenados']}, {'label':'/VPrelaciones', 'msg':['Error al guardar prelaciones']}, ]
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



@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
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
    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 'idPila':1}
    res['idPila'] = 1
    #Escala dependiente del proyecto
    res['fHistoria_opcionesPrioridad'] = [
      {'key':1, 'value':'Alta'},
      {'key':2, 'value':'Media'},
      {'key':3, 'value':'Baja'},
    ]


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    #GET parameter
    idHistoria = request.args['idHistoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 'idHistoria':1, 'idPila':1, 'codigo':'H01',
       'actores':[1,2], 'accion':2, 'objetivos':[1,3], 'tipo':1,
       'prioridad':2} 
    res['idPila'] = 1
    #Escala dependiente del proyecto
    res['fHistoria_opcionesPrioridad'] = [
      {'key':1, 'value':'Alta'},
      {'key':2, 'value':'Media'},
      {'key':3, 'value':'Baja'},
    ]
    res['data2'] = [ 
      {'idTarea':1, 'descripcion':'Sacarle jugo a una piedra'},
      {'idTarea':2, 'descripcion':'Pelar un mango'},
    ]
    res['idHistoria'] = 1


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistorias')
def VHistorias():
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
    #Datos de prueba
    res['idPila'] = 1
    res['data0'] = [
        {'idHistoria':1,'prioridad':'Alta', 'enunciado':'En tanto que cocinero puedo preparar una ratatuya para cenar'},
        {'idHistoria':2,'prioridad':'Media', 'enunciado':'En tanto que chef puedo hacer que los cocineros prepraren varios platos para cumplir con el munú'}
    ]
    

    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VPrelaciones')
def VPrelaciones():
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
    res['fPrelaciones'] = {'lista':[
      {'antecedente':1, 'consecuente':2},
      {'antecedente':2, 'consecuente':3}]}
    res['idPila'] = 1
    res['fPrelaciones_listaTareas'] = [
      {'key':1,'value':'Cortar el césped'},
      {'key':2,'value':'Hacer la siesta'},
      {'key':3,'value':'Almorzar'}
    ]

    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VPrioridades')
def VPrioridades():
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
    #Escala dependiente del proyecto
    res['fPrioridades_opcionesPrioridad'] = [
      {'key':1, 'value':'Alta'},
      {'key':2, 'value':'Media'},
      {'key':3, 'value':'Baja'},
    ]
    res['idPila'] = 1
    res['fPrioridades'] = {'idPila':1,
      'lista':[
        {'idHistoria':1,'prioridad':2, 'enunciado':'En tanto que cocinero puedo preparar una ratatuya para cenar'},
        {'idHistoria':2,'prioridad':2, 'enunciado':'En tanto que chef puedo hacer que los cocineros prepraren varios platos para cumplir con el munú'}
        ]}


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

