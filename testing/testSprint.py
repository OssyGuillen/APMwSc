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
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER,'Nxn3zzzz',1)
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

    # Prueba
    def testupdateSprintLeftLen140(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, 140*'T', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,'@jutdr tqdf lu mpgya')
        self.assertTrue(result)

    # Prueba
    def testupdateSprintIdBackLogInvalid(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1,'', 1, 'Wtqczr ul mds dfbyl')
        self.assertFalse(result)
'''
    # Casos Esquinas

    # Prueba 43
    def testupdateSprintLeftLen1RightLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('@',idBacklog)
        result    = aSprint.updateSprint('@',140*'V',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('@',idBacklog)
        aSprint.deleteSprint(140*'V',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 44
    def testupdateSprintLeftLen140RightLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint(140*'U',idBacklog)
        result    = aSprint.updateSprint(140*'U', 140*'M',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(140*'U',idBacklog)
        aSprint.deleteSprint(140*'M',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 45
    def testupdateSprintLeftLen140RightLen1(self):
        # Insertamos los datos necesarios.

        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint(20*'Llcmvr3',idBacklog)
        result    = aSprint.updateSprint(20*'Llcmvr3','@',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(20*'Llcmvr3',idBacklog)
        aSprint.deleteSprint('@',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 46
    def testupdateSprintLeftLen1RightLen1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('@',idBacklog)
        result    = aSprint.updateSprint('@','U',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('@',idBacklog)
        aSprint.deleteSprint('U',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 47
    def testupdateSprintLongDesc140AndIdBackLogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aSprint     = sprints()
        result   = aSprint.updateSprint(140*'U', 140*'M',2**28)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Casos Maliciosos

    # Prueba 48
    def testupdateSameName(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('Bvscqr pontfs ddbyl3z',idBacklog)
        result    = aSprint.updateSprint('Bvscqr pontfs ddbyl3z','Bvscqr pontfs ddbyl3z',idBacklog)
        self.assertTrue(result,"Modificación Válida")
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('Bvscqr pontfs ddbyl3z',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 49
    def testupdateSprintLeftLen0RightLen141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('',idBacklog)
        result    = aSprint.updateSprint('',20*'Llcmvr3' + 's',idBacklog)
        self.assertFalse(result, "Modificación válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 50
    def testupdateSprintLeftLen141RightLen141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint(20*'Llcmvr3' + 's',idBacklog)
        result    = aSprint.updateSprint(20*'Llcmvr3' + 's',20*'M@lcvra' + 's',idBacklog)
        self.assertFalse(result, "Modificación Válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 51
    def testupdateSprintLeftLen141RightLen0(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint(20*'Llcmvr3',idBacklog)
        result    = aSprint.updateSprint(20*'Llcmvr3','',idBacklog)
        self.assertFalse(result, "Modificación válida")
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(20*'Llcmvr3',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 52
    def testupdateSprintLeftNoneRightValidString(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        result    = aSprint.updateSprint(None,'Plxnyfyc@r 3strvtbjoia',idBacklog)
        self.assertFalse(result,"Modificación válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 53
    def testupdateSprintLeftValidStringRightNone(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('@patvr ponytgs do vodn',idBacklog)
        result    = aSprint.updateSprint('@patvr ponytgs do vodn',None,idBacklog)
        self.assertFalse(result, "Modificación válida")
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('@patvr ponytgs do vodn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 54
    def testupdateSprintIdNegative(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        aSprint.insertSprint('@patvr ponytgs do vodn',idBacklog)
        result    = aSprint.updateSprint('@patvr ponytgs do vodn','Nzzzcxn3',-1)
        self.assertFalse(result, "Modificación válida")
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('@patvr ponytgs do vodn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #         Pruebas para deleteSprint         #
    #############################################

    # Caso Inicial

    # Prueba 55
    def testDeleteAccionExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint('Us@r m2jop vlanct',idBacklog)
        # Inicio de la prueba.
        aSprint.deleteSprint('Us@r m2jop vlanct',idBacklog)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Casos Normales

    # Prueba 56      
    def testDeleteAccionDesc(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint('Dysdñvr prm@s',idBacklog)
        # Inicio de la prueba.
        result    = aSprint.deleteSprint('Dysdñvr prm@s',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 57
    def testDeleteAccionDescNotExits(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint('Dysdñvr prm@s',idBacklog)
        result    = aSprint.deleteSprint('Dysdñvr v3styfzzos',idBacklog)
        self.assertFalse(result)
        # Inicio de la prueba.
        aSprint.deleteSprint('Dysdñvr prm@s',idBacklog)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Casos Fronteras

    # Prueba 58
    def testDeleteAccionDescLen1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint('U',idBacklog)
        # Inicio de la prueba.
        result    = aSprint.deleteSprint('U',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 59
    def testDeleteAccionDescLen140(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId     = aBacklog.findName('Bxtyllz')
        idBacklog  = findId[0].BL_idBacklog
        aSprint       = sprints()
        aSprint.insertSprint(20*'Zewftsx',idBacklog)
        # Inicio de la prueba.
        result     = aSprint.deleteSprint(20*'Zewftsx',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 60
    def testDeleteAccionDescLen0(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId     = aBacklog.findName('Bxtyllz')
        idBacklog  = findId[0].BL_idBacklog
        aSprint       = sprints()
        aSprint.insertSprint('',idBacklog)
        # Inicio de la prueba.
        result     = aSprint.deleteSprint('',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 61
    def testDeleteAccionDescLen141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint(20*'Zewftsx'+'r',idBacklog)
        # Inicio de la prueba.
        result    = aSprint.deleteSprint(20*'Zewftsx'+'r',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 62
    def testDeleteAccionIdBacklogInvalid(self):
        # Inicio de la prueba.
        aSprint      = sprints()
        result    = aSprint.deleteSprint(20*'Zewftsx'+'r',0)
        self.assertFalse(result)

    # Casos Maliciosos

    # Prueba 63
    def testDeleteAccionDescNone(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aSprint      = sprints()
        result    = aSprint.deleteSprint(None,idBacklog)
        self.assertFalse(result,"Descripcion válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 64
    def testDeleteAccionNotString(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        aSprint      = sprints()
        aSprint.insertSprint(12345,idBacklog)
        # Inicio de la prueba.
        result    = aSprint.deleteSprint(12345,idBacklog)
        self.assertFalse(result,"Descripcion válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 65    
    def testDeleteAccionNotExist(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aSprint     = sprints()
        result   = aSprint.deleteSprint('Lys@a dp 3nfmsgzs xn vactayta',2)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 66
    def testDeleteAccionDescIdNegative(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aSprint     = sprints()
        result   = aSprint.deleteSprint('Lys@a dp 3nfmsgzs',-1)
        self.assertFalse(result,"Id válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
'''''