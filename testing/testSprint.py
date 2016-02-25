# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo sprintClass.py
sys.path.append('../app/scrum')

from app.scrum.sprintClass import *

class TestSprintClass(unittest.TestCase):
    
    #############################################      
    #         Pruebas para insertSprint         #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
    def testInsertSprintExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertSprint('VtXcyr pvntgs dw wydz',idBacklog)
        # Eliminamos los datos insertados.
        aAcc.deleteSprint('VtXcyr pvntgs dw wydz',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        

    # Casos Normales
      
    # Prueba 2
    def testInsertSprintElement(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint('Pqrmyt3 zlngfr',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteSprint('Pqrmyt3 zlngfr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                   
    # Prueba 3
    def testInsertSprintRepeatedElement(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint('Pqrmyt3 zlngfr',idBacklog)
        result1   = aAcc.insertSprint('Pqrmyt3 zlngfr',idBacklog)
        self.assertFalse(result1)
        # Eliminamos los datos insertados.
        aAcc.deleteSprint('Pqrmyt3 zlngfr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                
    # Casos Fronteras
       
    # Prueba 4
    def testInsertSprintShortDesc0(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint('',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 5
    def testInsertSprintLongDesc1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint('@',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteSprint('@',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 6
    def testInsertSprintLongDesc140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint(20*'LlWmcrl',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteSprint(20*'LlWmcrl',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 7
    def testInsertSprintLongDesc141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint(20*'LlWmcrl' + 'x',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 8
    def testInsertSprintIdBackLogInvalid(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertSprint('Wtqczr ul mds dfbyl',0)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Esquinas
        
    # Prueba 9
    def testInsertSprintIdBacklogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertSprint('DwfEndqr cun fw3rzv',88)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 10
    def testInsertSprintLongDesc140AndIdBackLogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertSprint(20*'LlWmcrl',99)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
                       
    # Casos Maliciosos
       
    # Prueba 11
    def testInsertNotString(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint(4350,idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 12
    def testInsertNoneString(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.insertSprint(None,idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 13
    def testInsertIdNegative(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertSprint('Nxn3zzzz',-1)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 14
    def testInsertIdString(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertSprint('Nxn3zzzz','1')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
                        
    #############################################      
    #         Pruebas para searchSprint         #
    #############################################
    '''
    # Caso Inicial
        
    # Prueba 15 
    def testsearchSprintExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertSprint('Vsdr mgjyq',idBacklog)
        aAcc.searchSprint('Vsdr mgjyq',idBacklog)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('Vsdr mgjyq',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Casos Fronteras
        
    # Prueba 16
    def testsearchAccionShortDesc0(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.searchAccion('',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 17
    def testsearchAccionShortDesc1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@',idBacklog)
        result    = aAcc.searchAccion('@',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 18
    def testsearchAccionShortDesc140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(20*'LlWmcrl',idBacklog)
        result    = aAcc.searchAccion(20*'LlWmcrl',idBacklog)
        self.assertNotEqual(result,[],"Accion no encontrada")
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(20*'LlWmcrl',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 19
    def testsearchAccionShortDesc141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints() 
        aAcc.insertAccion(20*'LlWmcrl' + 'm',idBacklog)
        result    = aAcc.searchAccion(20*'LlWmcrl' + 'm',idBacklog)
        self.assertFalse(result, "Accion Encontrada")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 20
    def testsearchAccionIdBackLogInvalid(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.insertAccion('Wtqczr ul mds dfbyl',0)
        result   = aAcc.searchAccion('Wtqczr ul mds dfbyl',0)
        self.assertFalse(result, "Accion Encontrada")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
        
    # Casos Esquinas

    # Prueba 21
    def testsearchAccionIdBacklogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('Wtqczr ul mds dfbyl',idBacklog)
        result    = aAcc.searchAccion('Wtqczr ul mds dfbyl',2**28)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('Wtqczr ul mds dfbyl',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        
  
    # Prueba 22
    def testsearchAccionLongDesc140AndIdBackLogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(20*'LlWmcrl',idBacklog)
        result    = aAcc.searchAccion(20*'LlWmcrl',2**28)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(20*'LlWmcrl',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
    
    # Caso Normal
        
    # Prueba 23
    def testsearchAccionDescNotExist(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.searchAccion('Lxdhvr cyn cqnfyznzs',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
             
    # Casos Maliciosos
         
    # Prueba 24
    def testsearchAccionNotString(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(4350,idBacklog)
        result    = aAcc.searchAccion(4350,idBacklog)
        self.assertEqual(result, [],'Accion Encontrada')
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 25 
    def testSearchNameNoneString(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.searchAccion(None,idBacklog)
        self.assertEqual(result, [],'Accion Encontrada')
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 26 
    def testSearchNameIdNegative(self):
        aAcc     = sprints()
        result   = aAcc.searchAccion('Nxnczzz',-1)
        self.assertEqual(result, [],'Accion Encontrada')
         
    # Prueba 27
    def testSearchNameIdString(self):
        aAcc     = sprints()
        result   = aAcc.searchAccion('Nxn3zzzz','1')
        self.assertEqual(result, [],'Accion Encontrada')
                          
    '''              
    #############################################      
    #       Pruebas para searchIdSprint         #
    #############################################  
    # Caso Inicial
            
    # Prueba 28  
    def testsearchIdSprintExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        aAcc      = sprints()
        aAcc.insertSprint('VsAr cdmzndqs qspxcywlts',idBacklog)
        result    = aAcc.searchSprint('VsAr cdmzndqs qspxcywlts',idBacklog)
        idAccion  = result[0].AC_idAccion
        # Inicio de la prueba.
        aAcc.searchIdAccion(idAccion)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('VsAr cdmzndqs qspxcywlts',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
  
    # Caso Normal
  
    # Prueba 29
    def testSearchIdTrue(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        aAcc      = sprints()
        aAcc.insertAccion('N@sEwx T',idBacklog)
        result    = aAcc.searchAccion('N@sEwx T',idBacklog)
        idAccion  = result[0].AC_idAccion
        # Inicio de la prueba.
        result    = aAcc.searchIdAccion(idAccion)
        self.assertNotEqual(result,[],"Elemento no encontrado")
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('N@sEwx T',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
  
    # Prueba 30                
    def testSearchIdNoAccion(self):
        # Inicio de la prueba. 
        aAcc     = sprints()
        result   = aAcc.searchIdAccion(2**28)
        self.assertEqual(result,[],"Elemento no encontrado")
  
    # Casos Maliciosos
  
    # Prueba 31
    def testSearchIdInvalid(self):
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.searchIdAccion(0)
        self.assertEqual(result,[], "Elemento no encontrado")
        
    # Prueba 32
    def testSearchIdString(self):
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.searchIdAccion('')
        self.assertEqual(result,[],"Elemento Insertado") 
        
    # Prueba 33
    def testSearchIdNoneString(self):
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.searchIdAccion(None)
        self.assertEqual(result,[],"Válido")  
         
    # Prueba 34
    def testSearchIdNegative(self):
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.searchIdAccion(-1)
        self.assertEqual(result,[],"Válido") 
                   
    #############################################      
    #        Pruebas para updateAccion          #
    #############################################  
 
    # Caso Inicial
        
    # Prueba 35
    def testupdateAccionExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('Yntdcvr an miqn',idBacklog)
        aAcc.updateAccion('Yntdcvr an miqn','Tnbdc3r xrmq asrtdmp',idBacklog)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('Yntdcvr an miqn',idBacklog)
        aAcc.deleteAccion('Tnbdc3r xrmq asrtdmp',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Casos Normales
        
    # Prueba 36
    def testupdateAccionDesc(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('Altomy Tnvfcgcyqn',idBacklog)
        result    = aAcc.updateAccion('Altomy Tnvfcgcyqn','T3rmynAr portwdp o txempz',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('Altomy Tnvfcgcyqn',idBacklog)
        aAcc.deleteAccion('T3rmynAr portwdp o txempz',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 37     
    def testupdateAccionDescNOtExist(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.updateAccion('Vsrr fvWjo','Usqr rpyD',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
             
    # Casos Fronteras
          
    # Prueba 38
    def testupdateAccionLeftLen1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@',idBacklog)
        result    = aAcc.updateAccion('@','Bvscqr pontfs ddbyl3z',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@',idBacklog)
        aAcc.deleteAccion('Bvscqr pontfs ddbyl3z',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 39
    def testupdateAccionRightLong1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@jutdr tqdf lu mpgya',idBacklog)
        result    = aAcc.updateAccion('@jutdr tqdf lu mpgya','@',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@',idBacklog)
        aAcc.deleteAccion('@jutdr tqdf lu mpgya',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 40         
    def testupdateAccionRightLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@jutdr tqdf lu mpgya',idBacklog)
        result    = aAcc.updateAccion('@jutdr tqdf lu mpgya',140*'T',idBacklog)
        self.assertTrue(result)    
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@jutdr tqdf lu mpgya',idBacklog)
        aAcc.deleteAccion(140*'T',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
    
    # Prueba 41
    def testupdateAccionLeftLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(140*'T',idBacklog)
        result    = aAcc.updateAccion(140*'T','@jutdr tqdf lu mpgya',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(140*'T',idBacklog)
        aAcc.deleteAccion('@jutdr tqdf lu mpgya',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 42
    def testupdateAccionIdBackLogInvalid(self):
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.updateAccion('Wtqczr ul mds dfbyl','@jutdr tqdf lu mpgya',0)
        self.assertFalse(result)
             
    # Casos Esquinas
         
    # Prueba 43
    def testupdateAccionLeftLen1RightLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@',idBacklog)
        result    = aAcc.updateAccion('@',140*'V',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@',idBacklog)
        aAcc.deleteAccion(140*'V',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
  
    # Prueba 44
    def testupdateAccionLeftLen140RightLen140(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(140*'U',idBacklog)
        result    = aAcc.updateAccion(140*'U', 140*'M',idBacklog)
        self.assertTrue(result) 
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(140*'U',idBacklog)
        aAcc.deleteAccion(140*'M',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 45
    def testupdateAccionLeftLen140RightLen1(self):
        # Insertamos los datos necesarios.
         
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(20*'Llcmvr3',idBacklog)
        result    = aAcc.updateAccion(20*'Llcmvr3','@',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(20*'Llcmvr3',idBacklog)
        aAcc.deleteAccion('@',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 46
    def testupdateAccionLeftLen1RightLen1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@',idBacklog)
        result    = aAcc.updateAccion('@','U',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@',idBacklog)
        aAcc.deleteAccion('U',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
 
    # Prueba 47
    def testupdateAccionLongDesc140AndIdBackLogNoExists(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.updateAccion(140*'U', 140*'M',2**28)
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
        aAcc      = sprints()
        aAcc.insertAccion('Bvscqr pontfs ddbyl3z',idBacklog)
        result    = aAcc.updateAccion('Bvscqr pontfs ddbyl3z','Bvscqr pontfs ddbyl3z',idBacklog)
        self.assertTrue(result,"Modificación Válida")
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('Bvscqr pontfs ddbyl3z',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 49
    def testupdateAccionLeftLen0RightLen141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('',idBacklog)
        result    = aAcc.updateAccion('',20*'Llcmvr3' + 's',idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 50
    def testupdateAccionLeftLen141RightLen141(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(20*'Llcmvr3' + 's',idBacklog)
        result    = aAcc.updateAccion(20*'Llcmvr3' + 's',20*'M@lcvra' + 's',idBacklog)
        self.assertFalse(result, "Modificación Válida") 
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 51
    def testupdateAccionLeftLen141RightLen0(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion(20*'Llcmvr3',idBacklog)
        result    = aAcc.updateAccion(20*'Llcmvr3','',idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        aAcc.deleteAccion(20*'Llcmvr3',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 52
    def testupdateAccionLeftNoneRightValidString(self):
        # Insertamos los datos necesarios.
        aBacklog   = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.updateAccion(None,'Plxnyfyc@r 3strvtbjoia',idBacklog)
        self.assertFalse(result,"Modificación válida") 
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 53
    def testupdateAccionLeftValidStringRightNone(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@patvr ponytgs do vodn',idBacklog)
        result    = aAcc.updateAccion('@patvr ponytgs do vodn',None,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@patvr ponytgs do vodn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
         
    # Prueba 54
    def testupdateAccionIdNegative(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        aAcc      = sprints()
        aAcc.insertAccion('@patvr ponytgs do vodn',idBacklog)
        result    = aAcc.updateAccion('@patvr ponytgs do vodn','Nzzzcxn3',-1)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        aAcc.deleteAccion('@patvr ponytgs do vodn',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
                         
    #############################################      
    #         Pruebas para deleteAccion         #
    #############################################
      
    # Caso Inicial
         
    # Prueba 55
    def testDeleteAccionExists(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
        aAcc      = sprints()
        aAcc.insertAccion('Us@r m2jop vlanct',idBacklog)
        # Inicio de la prueba.
        aAcc.deleteAccion('Us@r m2jop vlanct',idBacklog)
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
        aAcc      = sprints()
        aAcc.insertAccion('Dysdñvr prm@s',idBacklog)
        # Inicio de la prueba.
        result    = aAcc.deleteAccion('Dysdñvr prm@s',idBacklog)
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
        aAcc      = sprints()
        aAcc.insertAccion('Dysdñvr prm@s',idBacklog)
        result    = aAcc.deleteAccion('Dysdñvr v3styfzzos',idBacklog)
        self.assertFalse(result)
        # Inicio de la prueba.
        aAcc.deleteAccion('Dysdñvr prm@s',idBacklog)
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
        aAcc      = sprints()
        aAcc.insertAccion('U',idBacklog)
        # Inicio de la prueba.
        result    = aAcc.deleteAccion('U',idBacklog)
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
        aAcc       = sprints()
        aAcc.insertAccion(20*'Zewftsx',idBacklog)
        # Inicio de la prueba.
        result     = aAcc.deleteAccion(20*'Zewftsx',idBacklog)
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
        aAcc       = sprints()
        aAcc.insertAccion('',idBacklog)
        # Inicio de la prueba.
        result     = aAcc.deleteAccion('',idBacklog)
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
        aAcc      = sprints()
        aAcc.insertAccion(20*'Zewftsx'+'r',idBacklog)
        # Inicio de la prueba.
        result    = aAcc.deleteAccion(20*'Zewftsx'+'r',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')        
         
    # Prueba 62
    def testDeleteAccionIdBacklogInvalid(self):
        # Inicio de la prueba.
        aAcc      = sprints()
        result    = aAcc.deleteAccion(20*'Zewftsx'+'r',0)
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
        aAcc      = sprints()
        result    = aAcc.deleteAccion(None,idBacklog)
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
        aAcc      = sprints()
        aAcc.insertAccion(12345,idBacklog)
        # Inicio de la prueba.
        result    = aAcc.deleteAccion(12345,idBacklog)
        self.assertFalse(result,"Descripcion válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 65    
    def testDeleteAccionNotExist(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.deleteAccion('Lys@a dp 3nfmsgzs xn vactayta',2)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')
          
    # Prueba 66
    def testDeleteAccionDescIdNegative(self):
        # Insertamos los datos necesarios.
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','3nxmygzs db cAmpq',1)
        # Inicio de la prueba.
        aAcc     = sprints()
        result   = aAcc.deleteAccion('Lys@a dp 3nfmsgzs',-1)
        self.assertFalse(result,"Id válida")
        # Eliminamos los datos insertados.
        aBacklog.deleteProduct('Bxtyllz')        
 
# Fin de casos Accions