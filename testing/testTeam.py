# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from Team import *
from user import *
from role import *

class TestTeam(unittest.TestCase):
	
	#############################################      
    #         Pruebas para emptyTable           #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testEmptyTable(self):
    	team_object = team()
    	team_object.emptyTable()
    	
    #############################################      
    #         Pruebas para insertMiembro        #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testinsertMiembro(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Ejecutamos la funcion
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)  
        # Eliminamos los datos insertados
        team_object.deleteMiembro('userr','Actor',idBacklog)
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

    #############################################      
    #         Pruebas para deleteMiembro        #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testdeleteMiembro(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Ejecutamos la funcion
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)          
        team_object.deleteMiembro('userr','Actor',idBacklog)
        # Eliminamos los datos insertados
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Eliminar un usuario que no existe
    def testdeleteMiembroFalse(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Ejecutamos la funcion
        team_object = team()
        result = team_object.deleteMiembro('false_user','Actor',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')


if __name__ == '__main__':
    unittest.main()