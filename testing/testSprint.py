# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo sprintClass.py
sys.path.append('../app/scrum')

from app.scrum.sprintClass import *

class TestSprintClass(unittest.TestCase):

    def setUp(self):
        # Insertamos los datos necesarios.
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog

    def tearDown(self):
        # Eliminamos los datos insertados.
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #         Pruebas para insertSprint         #
    #############################################

    # Caso Inicial
    # Prueba 1
    def testInsertSprintExists(self):
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Casos Normales

    # Prueba 2
    def testInsertSprintElement(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 3
    def testInsertSprintRepeatedNumber(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        result1   = aSprint.insertSprint(1,'Haskndwkd akdmkwdmdwa',self.idBacklog)
        self.assertFalse(result1)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Casos Fronteras

    # Prueba 4
    def testInsertSprintShortDesc0(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'',self.idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 5
    def testInsertSprintLongDesc1(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,'@',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 6
    def testInsertSprintLongDesc140(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 7
    def testInsertSprintLongDesc141(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl' + 'x',self.idBacklog)
        self.assertFalse(result)
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 8
    def testInsertSprintIdBackLogInvalid(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Wtqczr ul mds dfbyl',0)
        self.assertFalse(result)

    # Casos Esquinas

    # Prueba 9
    def testInsertSprintIdBacklogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'DwfEndqr cun fw3rzv',80)
        self.assertFalse(result)

    # Prueba 10
    def testInsertSprintLongDesc140AndIdBackLogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,20*'LlWmcrl',99)
        self.assertFalse(result)

    def testInsertMaxSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER,'MAX_SPRINT_TEST',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(MAX_SPRINT_NUMBER,self.idBacklog)

    # Casos Maliciosos

    # Prueba
    def testInsertNotString(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,4350,self.idBacklog)
        self.assertFalse(result)

    # Prueba
    def testInsertNoneAsString(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,None,self.idBacklog)
        self.assertFalse(result)

    # Prueba
    def testInsertIdNegative(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Nxn3zzzz',-1)
        self.assertFalse(result)

    # Prueba
    def testInsertIdAsString(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Nxn3zzzz','1')
        self.assertFalse(result)

    def testInsertNegativeSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(-1,'Nxn3zzzz',self.idBacklog)
        self.assertFalse(result)

    def testInsertMaxOverflowSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER+1,'Nxn3zzzz',self.idBacklog)
        self.assertFalse(result)

    #############################################      
    #       Pruebas para searchIdSprint         #
    #############################################  
    # Caso Inicial

    # Prueba
    def testsearchIdSprintExists(self):
        # Insertamos los datos necesarios.
        aSprint        = sprints()
        aSprint.insertSprint(1,'VsAr cdmzndqs qspxcywlts',self.idBacklog)
        # Inicio de la prueba.
        foundSprint = aSprint.searchIdSprint(1, self.idBacklog)[0]
        self.assertEqual(foundSprint.S_sprintDescription, 'VsAr cdmzndqs qspxcywlts')
        self.assertEqual(foundSprint.S_numero, 1)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('VsAr cdmzndqs qspxcywlts',self.idBacklog)

    # Caso Normal

    # Prueba
    def testSearchIdNotExist(self):
        # Insertamos los datos necesarios.
        aSprint        = sprints()
        aSprint.insertSprint(1,'VsAr cdmzndqs qspxcywlts',self.idBacklog)
        # Inicio de la prueba.
        foundSprintId = aSprint.searchIdSprint(100, self.idBacklog)
        self.assertEqual(foundSprintId,[])
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('VsAr cdmzndqs qspxcywlts',self.idBacklog)

    # Prueba
    def testSearchIdNoBacklog(self):
        # Inicio de la prueba. 
        aSprint     = sprints()
        result   = aSprint.searchIdSprint(1, None)
        self.assertEqual(result,[],"Elemento no encontrado")

    # Casos Maliciosos
    # Prueba
    def testSearchIdInvalid(self):
        # Inicio de la prueba.
        aSprint     = sprints()
        result   = aSprint.searchIdSprint(0,self.idBacklog)
        self.assertEqual(result,[],"Elemento no encontrado")

    # Prueba
    def testSearchIdString(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint('',self.idBacklog)
        self.assertEqual(result,[],"Elemento no encontrado")

    # Prueba
    def testSearchIdNoneString(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint(1, None)
        self.assertEqual(result,[],"Válido")

    # Prueba
    def testSearchIdNegative(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint(-1, self.idBacklog)
        self.assertEqual(result,[],"Válido")

    #############################################
    #        Pruebas para updateSprint          #
    #############################################  

    # Caso Inicial

    # Prueba
    def testupdateSprintExists(self):
        aSprint      = sprints()
        aSprint.insertSprint(1,'Yntdcvr an miqn',self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 2 , 'Tnbdc3r xrmq asrtdmp')
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        aSprint.deleteSprint(2,self.idBacklog)

    # Casos Normales
    # Prueba
    def testupdateSprintDesc(self):
        aSprint   = sprints()
        aSprint.insertSprint(1,'Altomy Tnvfcgcyqn',self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 1 , 'Tnbdc3r xrmq asrtdmp')
        sprintUpdate = aSprint.searchIdSprint(1,self.idBacklog)[0]
        self.assertEqual(sprintUpdate.S_sprintDescription, 'Tnbdc3r xrmq asrtdmp')
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba
    def testupdateSprintNumber(self):
        aSprint   = sprints()
        aSprint.insertSprint(1,'Altomy Tnvfcgcyqn', self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 2 ,'Altomy Tnvfcgcyqn')
        sprintUpdate = aSprint.searchIdSprint(2,self.idBacklog)[0]
        self.assertNotEqual(sprintUpdate, [])
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        aSprint.deleteSprint(2,self.idBacklog)

    # Prueba
    def testupdateSprintDescNOtExist(self):
        aSprint      = sprints()
        result = aSprint.updateSprint(1, self.idBacklog, 2 ,'Altomy Tnvfcgcyqn')
        self.assertFalse(result)

    # Casos Fronteras

    # Prueba
    def testupdateSprintLeftLen1(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog,1,'Bvscqr pontfs ddbyl3z')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba
    def testupdateSprintRightLong1(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,'@')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba
    def testupdateSprintRightLen140(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,140*'T')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba
    def testupdateSprintLeftLen140(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, 140*'T', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,'@jutdr tqdf lu mpgya')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba
    def testupdateSprintIdBackLogInvalid(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1,'', 1, 'Wtqczr ul mds dfbyl')
        self.assertFalse(result)

    #############################################
    #         Pruebas para deleteSprint         #
    ##############################################
    # Caso Inicial
    # Prueba
    def testDeletSprintExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
        result   = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        oSprint.deleteSprint(1,self.idBacklog)


    # Casos Normales

    # Prueba
    def testDeleteValidSprint(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(2,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(2,self.idBacklog)
        self.assertTrue(result)


    # Casos Fronteras internas
 
    # Prueba
    def testDeleteSprintNum1ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1,self.idBacklog)
        self.assertTrue(result) 

    #Prueba
    def testDeleteSprintNum1000ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1000,self.idBacklog)
        self.assertTrue(result)

    
    # Casos Fronteras internas

    #Prueba
    def testDeleteSprintNum0ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(0,self.idBacklog)
        self.assertFalse(result)  

    #Prueba
    def testDeleteSprintNum1001ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1001,self.idBacklog)
        self.assertFalse(result) 

    #Prueba
    def testDeleteSprintNegativeNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(-1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(-1,self.idBacklog)
        self.assertFalse(result) 

    #Prueba
    def testDeleteSprintStringNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint('1','VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint('1',self.idBacklog)
        self.assertFalse(result) 

    #Prueba
    def testDeleteSprintNullNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(None,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(None,self.idBacklog)
        self.assertFalse(result) 
    '''
    '''
    #Prueba
    def testDeleteSprintNotNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(100,self.idBacklog)
        self.assertFalse(result)