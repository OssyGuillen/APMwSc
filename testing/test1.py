# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from sprintClass import *
from meetingClass import *
from elementMeetingClass import *
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
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1', 'Presencial', idASprint)
        findIdMeeting = aMeeting.searchMeeting(date0, idASprint)
        idMeeting = findIdMeeting[0].SM_idSprintMeeting

        print ("ID MEETING", idMeeting)

        # Creamos el elemento
        aElement = elementMeeting()
        #result =  aElement.emptyTable()
        #self.assertTrue(result)
        result = aElement.insertElement('challenges', 'planned', 'done', idMeeting, 'user1')
        #self.assertTrue(result)
        get = aElement.getElements(idMeeting)
        print("GET", get)
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idMeeting)
        elementID = foundElementId[0].EM_idElementMeeting

        print ("ELEMENT ID", elementID)
        x = aElement.updateElement(elementID, 'newChallenges', 'newPlanned', 'newDone', idMeeting, 'user1')
        x = aElement.deleteElement(elementID, idMeeting)
        self.assertTrue(x)

        # Eliminamos los datos insertados.
        result = aMeeting.deleteMeeting(date0,idASprint)
        self.assertTrue(result)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')



if __name__ == '__main__':
    unittest.main()