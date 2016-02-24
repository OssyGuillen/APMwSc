# -*- coding: utf-8 -*-
from flask                       import request, session, Blueprint, json
from app.scrum.role              import *
from app.scrum.actorsUserHistory import *

actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res     = results[1]
    
    # Obtenemos el id del producto
    idPila  = int(session['idPila'])
    
    if params != {}:    
        # Extraemos los datos
        nameActor = params['nombre']
        descActor = params['descripcion'] 
        
        # Insertamos el actor
        oActor   = role()
        inserted = oActor.insertActor(nameActor,descActor,idPila)
        if inserted:
            res = results[0]
    
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@actor.route('/actor/AElimActor')
def AElimActor():
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Actor eliminado']}, {'label':'/VProducto', 'msg':['No se pudo eliminar este actor']}, ]
    res     = results[1]
    
    # Obtenemos el id del producto y de la acción
    idPila  = int(session['idPila'])
    idActor = int(session['idActor'])
    
    # Conseguimos el actor a eliminar 
    oActor = role()
    found  = oActor.findIdActor(idActor)
    
    oActorUserHistory = actorsUserHistory()
    result            = oActorUserHistory.searchidUserHistoryIdActors(idActor)

    # Verificamos si el actor está asociado a una historia
    if (result == []):
        deleted = oActor.deleteActor(found[0].A_nameActor,idPila)
    
        if deleted:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VProducto', 'msg':['Error al modificar actor']}, ]
    res     = results[1]
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)    

    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])

    # Extraemos los parámetros
    idActor      = params['idActor'] 
    newNameActor = params['nombre']
    newDescActor = params['descripcion'] 
    
    # Conseguimos el actor a modificar  
    oActor = role()
    found  = oActor.findIdActor(idActor)

    # Modificamos el actor deseado
    result = oActor.updateActor(found[0].A_nameActor , newNameActor, newDescActor,idPila)    
    
    if result:
        res = results[0]
    
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    
    return json.dumps(res)



@actor.route('/actor/VActor')
def VActor():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto y de la acción
    idPila  = int(session['idPila'])
    idActor = int(request.args.get('idActor'))

    if "actor" in session:
        res['actor']=session['actor']
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Buscamos el actor actual
    oActor = role()
    result = oActor.findIdActor(idActor) 
    
    res['fActor'] = {'idActor':idActor, 'nombre':result[0].A_nameActor, 'descripcion':result[0].A_actorDescription}    
    res['idPila'] = idPila
    session['idActor'] = idActor
   
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
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
