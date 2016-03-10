# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from sprintClass import *
from meetingClass import *
from role import *

class TestElementMeeting(unittest.TestCase):

    def testDeleteMeetingTrue(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        print ("IDSPRINT",idASprint)
        ## Creamos el meeting
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2015'
        date2 = '2015-02-03'
        aMeeting = meeting()
        a = aMeeting.getMeetings(3)
        print ("A", a)
        b = aMeeting.getMeetings(idASprint)
        print("B",b)



        #aMeeting.searchMeeting(date0, idSprint):
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1', 'Presencial', idASprint)
        x = aMeeting.searchMeeting(date0,idASprint)
        print(x)

        # Eliminamos los datos insertados.
        result = aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        #self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()