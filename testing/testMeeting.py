# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from sprintClass import *
from meetingClass import *
from role import *

class TestMeeting(unittest.TestCase):
    #############################################      
    #         Pruebas para emptyTable           #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testEmptyTable(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
    
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        aMeeting = meeting () 
        print (aMeeting.getMeetings(1))
        date = datetime.date(2015,8,9)
        date1 = datetime.date(2018,8,9)
        date2 = datetime.date.today()
        result = aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', 1)
        self.assertTrue(result)
        print (aMeeting.getMeetings(1))
        result = aMeeting.updateMeeting(date,date1, 'A1', 'S1', 'C1', 1)
        self.assertFalse(result)
        result = aMeeting.updateMeeting(date,date2, 'A2', 'S2', 'C2', 1)
        self.assertTrue(result)
        print (aMeeting.getMeetings(1))
        result = aMeeting.deleteMeeting(date1,1)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        self.aBacklog.deleteProduct('Bxtyllz')
        aSprint.deleteSprint(1,self.idBacklog)
        aMeeting.deleteMeeting(date2,1)
        print (aMeeting.getMeetings(1))


if __name__ == '__main__':
    unittest.main()