# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo objective.py
sys.path.append('app/scrum')
from objective import *

# Definicion de constantes
CONST_MIN_ID = 1


class objectivesUserHistory(object):
    '''Clase que permite manejar los objetivos asociados a una historia de manera persistente'''
    
    def insertObjectiveAsociatedInUserHistory(self,id_Objective, id_userHistory):
        '''Permite insertar un objetivo a una historia de usuario'''
        
        checkIdObjective = type(id_Objective) == int and id_Objective >= CONST_MIN_ID
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID
        
        if checkIdObjective and checkUserHistory:
            oObjective     = clsObjective.query.filter_by(O_idObjective = id_Objective).all()
            oIdUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory  = id_userHistory).all()
            
            if oObjective != [] and oIdUserHistory != []:
                newObj = clsObjectivesUserHistory(id_Objective,id_userHistory)
                db.session.add(newObj)
                db.session.commit()
                return True
        return False


    def idObjectivesAsociatedToUserHistory(self,id_userHistory):
        '''Permite obtener los ids de los objetivos asociados a una historia de usuario'''
        
        checkIdUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID
        
        idsList = []
        if checkIdUserHistory:
            result  = clsObjectivesUserHistory.query.filter_by(OUH_idUserHistory = id_userHistory)
            
            for obj in result:
                idsList.append(obj.OUH_idObjective)
        return idsList
        
        
    def searchidUserHistoryIdObjective(self, idObjective):
        '''Permite obtener los ids de las historias de usuario que contiene el idObjective'''
        
        checkIdObjective = type(idObjective) == int and idObjective >= CONST_MIN_ID

        if checkIdObjective:
            result = clsObjectivesUserHistory.query.filter_by(OUH_idObjective = idObjective).all()
            return result
        return ([])
        

    def deleteObjectiveAsociatedInUserHistory(self,id_Objective, id_userHistory):
        '''Permite eliminar un actor de una historia de usuario'''
        
        checkIdObjective = type(id_Objective) == int and id_Objective >= CONST_MIN_ID
        checkUserHistory = type(id_userHistory) == int and id_userHistory >= CONST_MIN_ID

        if checkIdObjective and checkUserHistory:
            oObjective = clsObjectivesUserHistory.query.filter_by(OUH_idObjective = id_Objective,OUH_idUserHistory = id_userHistory).all()
            
            if oObjective != []:
                for i in oObjective:
                    db.session.delete(i)
                db.session.commit()
                return True
        return False
    
# Fin Clase objectivesUserHistory