# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes.
MIN_ID                 = 1
MIN_SPRINT_DESCRIPTION = 1
MAX_SPRINT_DESCRIPTION = 140


class sprints(object):
    '''Clase que permite manejar los sprints de manera persistente'''

    def insertSprint(self, sprintNumber, sprintDescription, idBacklog):

        '''Permite insertar una Sprint asociado a un producto'''   
        
        checkTypeDescription = type(sprintDescription) == str
        checkTypeId          = type(idBacklog) == int
        checkTypeNumber      = type(sprintNumber) == int

        if checkTypeDescription and checkTypeId and checkTypeNumber:
            checkLongSprintDescription = MIN_SPRINT_DESCRIPTION <= len(sprintDescription) <= MAX_SPRINT_DESCRIPTION
            checkLongId                = MIN_ID <= idBacklog
        
            if checkLongSprintDescription and checkLongId:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()                      
                
                if foundBacklog != []:
                    foundSprints = clsSprint.query.filter_by(S_idBacklog = idBacklog).all()

                    foundSprintDesc = []
                    for desc in foundSprints:
                        if desc.S_sprintDescription.lower()  == sprintDescription.lower():
                            foundSprintDesc.append(desc)
                            break
                         
                    if foundSprintDesc == []:

                        newSprint = clsSprint(sprintNumber, sprintDescription, idBacklog)

                        db.session.add(newSprint)
                        db.session.commit()
                        return True
        return False


# Fin Clase Sprint