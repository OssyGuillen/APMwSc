# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

class precedence(object):
    def gelAllPrecedences(self, idPila):
        return

    def insertPrecedence(self, idFirstTask, idSecondTask, idPila):
        if (idFirstTask != idSecondTask):
            if self.doesNotMakeLoops(idFirstTask, idSecondTask):
                newPrecedence = clsPrecedence(idFirstTask, idSecondTask, idPila)
                db.session.add(newPrecedence)
                db.session.commit()
            else:
                print('Error')
        else:
            print('Error')
        return


    def deletePrecedence(self, idFirstTask, idSecondTask):
        return

    def searchTaskByPrec(self, idTask):
        return

    def searchTaskByCons(self, idTask):
        return

    def doesNotMakeLoops(self, idFirstTask, idSecondTask):
        return True