# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from user import *
from role import *

class TestUser(unittest.TestCase):

    ##########################################      
    #        Pruebas para InsertUser         #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 1
    def testInsertUserExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog  
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sah','ehfah','al', '@ls',idActor)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Casos frontera

    # Prueba 2   
    def testInsertUserTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sah','ehfahw','alir893b1','@ls',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
                   
    # Prueba 3
    def testInsertUserFalse(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser('sah','ehfah','al', '@ls',6000)
        self.assertFalse(result)
           
    # Prueba 4
    def testInsertUserEmptyUsername(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result = oUser.insertUser('sah','','al','@?lds',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 5
    def testInsertUserUsernameLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid', 'a','1223478364', 'xxx@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('a')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')  
   
    # Prueba 6
    def testInsertUserUsernameLength17(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 7
    def testInsertUserUsernameLength16(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid', 'jksjdfdjvkjdfuhf','122346768', 'yzyyxxx@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('jksjdfdjvkjdfuhf')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 8
    def testInsertUserUsernameLength15(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog  
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid', 'wjfr9olpsmfkreo','1225676834', 'xfeexx@fgmail.com',idActor)
        self.assertTrue(result) 
        # Eliminamos los datos insertados.
        oUser.deleteUser('wjfr9olpsmfkreo')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 9
    def testInsertUserUserNameLength8(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba. 
        result    = oUser.insertUser('sahid', 'wiekfprm','1223463637', 'yffe@ldv.gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('wiekfprm')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
             
    # Prueba 10
    def testInsertUserFullnameLength51(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx Rryfs Vrlrncyu kjhdj kjhvjfdbhjdcmkd', 'jksjdfdj vkjdfuhf','12234', 'xxx@gmail.com',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 11
    def testInsertUserFullnameLength50(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sdhtd Pdtrycrt Rtyys Vslcncta kjhdj kjhvjfdbhjdcmk', 'jksjdfdj__','1223485953', 'xx__x@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('jksjdfdj__') 
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')      
                  
    # Prueba 12
    def testInsertUserFullnameLength49(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', 'jpvkjdfuhf','8475312234', 'xyyy@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('jpvkjdfuhf') 
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
         
    # Prueba 13
    def testInsertUserFullnameLength25(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('Pxtrscre Rtyts Vqlfncfa25', 'patkjdfuhf','1223467843', 'patx@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('patkjdfuhf')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 14
    def testInsertUserEmptyFullname(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('', 'patkjdfuhf','12234', 'patx@gmail.com',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 15
    def testInsertUserFullnameLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('P', 'patkfhf_1','122374834', 'paddtx@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('patkfhf_1')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 16
    def testInsertUserEmailLength31(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx', 'tdd ','12d234', '10-10603-10-10916ing@ldc.usb.ve',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 17
    def testInsertUserEmptyEmail(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx', 'tdd ','12d234', '',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 18
    def testInsertUserEmailLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx', 'tdd_1','12d2345678','@',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('tdd_1')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')        
         
    # Prueba 19
    def testInsertUserEmailLength30(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx', 'tdd_2','12d2356784', '123167890patricia_v@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('tdd_2')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 20
    def testInsertUserEmailLength29(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sxhyd Pxtrycyx', 'tdd_3','12d2343434', '123167890patriciav@gmail.com',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('tdd_3')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 21
    def testInsertUserPasswordLength201(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('pat', 'ehfer_23',100*'12' + 'e', '2@ls',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 22
    def testInsertUserEmptyPassword(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sah', 'ehfadh_2','', '3@ls',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 23
    def testInsertUserPasswordLength199(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sah', 'ehf_1',199*'e', 'po@rls',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehf_1')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 24
    def testInsertUserPasswordLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sr', 'er3r_1','1', 'desm@ld.s',idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('er3r_1')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 25
    def testInsertUserPasswordLength2(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.insertUser('sah', 'frkfe_1','qi', 'fefef_t@l.ss', idActor)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('frkfe_1')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 26
    def testInsertUserNoneRole(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser('srgfer', 'pw74b_r','efoewfwe1', 'tarea@hot.com', None)
        self.assertFalse(result)
   
    # Prueba 27
    def testInsertUserInvalidIdRole(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser('utdf R', 'olpo','efefefr3', 'nonemail@,mail.cpom','8')
        self.assertFalse(result)
           
    # Caso Malicia

    # Prueba 28
    def testInsertUserInvalidStringIdRole(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser('sahid', 'a','12234', 'xxx@gmail.com','b')
        self.assertFalse(result)
           
    # Prueba 29
    def testInsertUserInvalidParams(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser('', '','', '', None)
        self.assertFalse(result)

    # Prueba 30
    def testInsertUserNoneParams(self):
        oUser     = user()
        # Inicio de la prueba.
        result    = oUser.insertUser(None, None,None, None,None)
        self.assertFalse(result)
                      
    # Caso esquina

    # Prueba 31
    def testInsertUserInvalidForeignIdRole(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.insertUser('fiee0 ee', 'q84-g0gs','wdwd94', 'ffjfor@w.pol',9000)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
  
     ##########################################      
     #   Suite de Pruebas para searchUser     #
     ##########################################
      
    # Caso Inicial

    # Prueba 32
    def testSearchUserExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        result    = oUser.searchUser('ehfah')
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
  
    #Caso Frontera
    
    # Prueba 33
    def testSearchUserTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog  
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('nombre','ehfah','12345678','ef@fg.com',idActor)
        # Inicio de la prueba. 
        result    = oUser.searchUser('ehfah')
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
             
    # Prueba 34
    def testSearchUserUsernameLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('nombreA','a','12345678','a@g.com',idActor)
        # Inicio de la prueba. 
        result    = oUser.searchUser('a')
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('a')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
     
    # Prueba 35
    def testSearchUserUsarnameLength6(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('new uswer','jksjdfdjvkjdfuhf','12345678','nuevo@.com',idActor)
        # Inicio de la prueba. 
        result    = oUser.searchUser('jksjdfdjvkjdfuhf')
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('new uswer')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
      
    # Prueba 36
    def testSearchUserUsernameLength7(self):  
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('fullname','jksjdfdj vkjdfuhf','12345678','email@',idActor)
        # Inicio de la prueba. 
        result    = oUser.searchUser('jksjdfdj vkjdfuhf')
        self.assertEqual([],result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
  
    # Caso Esquina

    # Prueba 37
    def testSearchUserUserNameNotInserted(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba. 
        result = oUser.searchUser('PatriciaValencia')
        self.assertEqual([],result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
  
    # Prueba 38
    def testSearchUserUsernameLength8(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('fullname','wiekfprm','123456784','eail@nuevo',idActor)
        # Inicio de la prueba. 
        result = oUser.searchUser('wiekfprm')
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('wiekfprm')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
  
    # Caso Malicia 

    # Prueba 39
    def testSearchUserEmptyUsername(self):
        # Insertamos los datos necesarios.
        oUser     = user()
        # Inicio de la prueba. 
        result = oUser.searchUser('')
        self.assertEqual([],result)
        # Eliminamos los datos insertados.

    # Prueba 40            
    def testSearchUserNoneParam(self):
        oUser     = user()
        # Inicio de la prueba. 
        result = oUser.searchUser(None)
        self.assertEqual([],result)
  
    ##########################################      
    #   Suite de Pruebas para UpdateUser     #
    ##########################################

    # Caso Inicial

    # Prueba 41        
    def testUpdateUserTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('loquesea','ehfah','12345678','cosa',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('xd','ehfah','ldow1qeqt', 'o123ifhweief@ef',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Frontera

    # Prueba 42 
    def testUpdateUserFalse(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('valido', 'ehfah', 'ldowf4r42q', 'oifhwe@fw',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser(None, 'ehfah', 'ldowqeq', 'oifhweiofw',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 43    
    def testUpdateUserNonePassword(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('yloqdd', 'ehfah', '123456789', 'oieeniofefw',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('y', 'ehfah', None, 'oieeniofefw',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 44        
    def testUpdateUserNoneDescription(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('loqwew', 'ehfah', 'ldoee22wqeq', 'nuevoemaild', idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('loq', 'ehfah', 'ldowqeq', '',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 45           
    def testUpdateUserElementToUpdateDoesNotExist(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('loer3q', 'ehfah', '123163r378012wd', 'frrwfwfe',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('loq', 'ehfah','123167891012wd', 'fwfwfe',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 46    
    def testUpdateUserInvalidNumberRole(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        # Inicio de la prueba.
        result    = oUser.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfefwfe', 4000)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 47
    def testUpdateUserInvalidStringRole(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        # Inicio de la prueba.
        result    = oUser.updateUser( 'lfoq', 'ehfah', '1231612wd', 'fwfe@fwfe','a')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')    

    # Prueba 48     
    def testUpdateUserNoneUsername(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog  
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        # Inicio de la prueba.
        result    = oUser.updateUser( 'lfoq', None, '1231612wd', 'fwf@@efwfe',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 49    
    def testUpdateUserInvalidParams(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser( '', '', '', '', None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 50     
    def testUpdateUserNoneParams(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser( None, None,  None, None, None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 51     
    def testUpdateUserValidUsernameInvalidOtherParams(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser( None, 'ehfah', None, None, None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 52     
    def testUpdateUserMaxNumberCharactersAllowed(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser(50*'a','ehfah','condieciseischar','cuenta30a@prueba.usb.ve',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 53 
    def testUpdateUserExternalBorder(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('mas cincuenta caracteres en el nombre con espacios_','ehfah','condieci_seischar','cuenta30charpara@_prueba.usb.ve',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 54     
    def testUpdateUserInternalBorder(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser('mas cincuenta caracteres en el nombre con espacio','ehfah','condieciseischa','cuenta30charpar@prueba.usb.ve',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 55     
    def testUpdateUserNotfound(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog  
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser( 'wdwdwd', 'ehfah', '1234567890', 'nuebee3@',idActor)
        # Inicio de la prueba.
        result    = oUser.updateUser( 'mas cincuenta caracteres ', 'prueba_admin', 'condieciseischar', 'cuentanueva@prueba.usb.ve',idActor)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
     
    ##########################################      
    #   Suite de Pruebas para DeleteUser     #
    ##########################################
     
    # Caso Inicial

    # Prueba 56     
    def testUserDeleteExist(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oUser.deleteUser('ehfah')

    #vCaso Frontera

    # Prueba 57     
    def testUserDeleteTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('urown','wiekfprm','1234322249','email@nee',idActor)
        # Inicio de la prueba.
        result    = oUser.deleteUser('wiekfprm')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
      
    # Prueba 58     
    def testUserDeleteFalse(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.deleteUser('wiekfprm')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 59         
    def testUserDeleteUsernameLength1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('nombrea','a','passworda12','emaila',idActor)
        # Inicio de la prueba.
        result    = oUser.deleteUser('a')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
          
    # Prueba 60       
    def testUserDeleteUsernameLength16(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('nombre','jksjdfdjvkjdfuhf','1234567890','emaildwd@',idActor)
        # Inicio de la prueba.
        result    = oUser.deleteUser('jksjdfdjvkjdfuhf')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 61       
    def testUserDeleteUsernameLength17(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.deleteUser('jksjdfdj vkjdfuhf')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 62
    def testUserDeleteUsernameLength15(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('nombre','wjfr9olpsmfkreo','1234567890','emailen',idActor)
        # Inicio de la prueba.
        result    = oUser.deleteUser('wjfr9olpsmfkreo')
        self.assertTrue(result) 
        # Eliminamos los datos insertados.
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia

    # Prueba 63     
    def testUserDeleteEmptyUsername(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.deleteUser('')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')
              
    # Prueba 64         
    def testUserDeleteNoneParam(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.deleteUser(None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs')     
     
    # Prueba 65     
    def testUserDeleteNumberParam(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        # Inicio de la prueba.
        result    = oUser.deleteUser(13)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Pxrsynzjxs') 

    ##########################################      
    #   Suite de Pruebas para findEmail      #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 66      
    def testUserFindEmailExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfah','al', '@ls', idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail('@ls')
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso normal

    # Prueba 67   
    def testUserFindEmailTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','@ls',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail('@ls')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso frontera
                   
    # Prueba 68
    def testUserFindEmailString1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','l',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail('l')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 69
    def testUserFindEmailString2(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','ls',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail('ls')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 70
    def testUserFindEmailString30(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1',10*'@ls',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail(10*'@ls')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 71
    def testUserFindEmailString29(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail(7*'@las'+ 's')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia
    
    # Prueba 72
    def testUserFindEmailString0(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail('')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 73
    def testUserFindEmailNone(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','alas',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail(None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 74
    def testUserFindEmailInteger(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','alas',idActor)
        # Inicio de la prueba.
        result    = oUser.findEmail(1)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    ##########################################      
    #   Suite de Pruebas para isFound        #
    ##########################################
    
    # Caso Inicial
 
    # Prueba 75
    def testUserIsFoundExist(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfah','al', '@ls', idActor)
        # Inicio de la prueba.
        result    = oUser.isFound('ehfah')
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso normal

    # Prueba 76   
    def testUserIsFoundTrue(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','@ls',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound('ehfahw')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso frontera
                   
    # Prueba 77
    def testUserIsFoundString1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','e','alir893b1','ldddf',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound('e')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('e')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 78
    def testUserIsFoundString2(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','eh','alir893b1','lfdfs',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound('eh')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('eh')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
            
    # Prueba 79
    def testUserFindEmailString16(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah',4*'ehfa','alir893b1','@ls',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound(4*'ehfa')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser(4*'ehfa')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
   
    # Prueba 80
    def testUserIsFoundString15(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah',3*'ehfah','alir893b1','@las',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound(3*'ehfah')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser(3*'ehfah')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Caso Malicia
    
    # Prueba 81
    def testUserIsFoundString0(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1',7*'@las'+ 's',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound('')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
           
    # Prueba 82
    def testUserIsFoundNone(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','alas',idActor)
        # Inicio de la prueba.
        result    = oUser.isFound(None)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')

    # Prueba 83
    def testUserIsFoundInteger(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oRole     = role()
        oUser     = user()
        oBacklog.insertBacklog('Pxrsynzjxs','Dxsyñz dy rzlys',1)
        findId    = oBacklog.findName('Pxrsynzjxs')
        idBacklog = findId[0].BL_idBacklog 
        oRole.insertActor('Xsxyrvz','Mxnyjxdzr',idBacklog)
        result    = oRole.findNameActor('Xsxyrvz',idBacklog)
        idActor   = result[0].A_idActor
        oUser.insertUser('sah','ehfahw','alir893b1','alas',idActor)
        # Inicio de la prueba. 
        result    = oUser.isFound(1)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oUser.deleteUser('ehfahw')
        oRole.deleteActor('Xsxyrvz',idBacklog)
        oBacklog.deleteProduct('Pxrsynzjxs')
        
# Fin de casos User