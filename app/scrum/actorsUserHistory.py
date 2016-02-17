# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo role.py
sys.path.append('app/scrum')
from role import *

# Definicion de constantes
CONST_MIN_ID = 1

class actorsUserHistory(object):
    '''Clase que permite manejar los objetivos asociados a una historia de manera persistente'''
    
    def insertActorAsociatedInUserHistory(self,id_Actor, id_userHistory):
        '''Permite insertar un actor a una historia de usuario'''
        
        checkIdActor     = type(id_Actor) == int and id_Actor >= CONST_MIN_ID
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID
        
        if checkIdActor and checkUserHistory:
            oActor         = clsActor.query.filter_by(A_idActor = id_Actor).all()
            oIdUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = id_userHistory).all()
            
            if oActor != [] and oIdUserHistory != []:
                newAct = clsActorsUserHistory(id_Actor,id_userHistory)
                db.session.add(newAct)
                db.session.commit()
                return True
        return False
    
        
    def idActorsAsociatedToUserHistory(self, id_userHistory):
        '''Permite obtener los ids de los actores asociados a una historia de usuario'''
        
        checkIdUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID
        
        idsList = []
        if checkIdUserHistory:
            result = clsActorsUserHistory.query.filter_by(AUH_idUserHistory = id_userHistory).all()
            
            for act in result:
                idsList.append(act.AUH_idActor)
        return idsList
    
        
    def searchidUserHistoryIdActors(self, idActor):
        '''Permite obtener los ids de las historias de usuario que contiene el idActor'''
        
        checkIdActor = type(idActor) == int and idActor >= CONST_MIN_ID
        
        if checkIdActor:
            result = clsActorsUserHistory.query.filter_by(AUH_idActor = idActor).all()
            return result
                  
        
    def deleteActorAsociatedInUserHistory(self,id_Actor, id_userHistory):
        '''Permite eliminar un actor de una historia de usuario'''
        
        checkIdActor     = type(id_Actor) == int and id_Actor >= CONST_MIN_ID
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID

        if checkIdActor and checkUserHistory:
            oActor = clsActorsUserHistory.query.filter_by(AUH_idActor = id_Actor,AUH_idUserHistory = id_userHistory).all()
            
            if oActor != []:
                for i in oActor:
                    db.session.delete(i)
                db.session.commit()
                return True
        return False
    
# Fin Clase actorsUserHistory