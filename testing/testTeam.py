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

    # Probar que hay elementos en team
    def testEmptyTableFalse(self):
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
        # Agregamos un usuario a team
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)
        # Ejecutamos la funcion
        result = team_object.emptyTable()
        self.assertFalse(result)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('userr','Actor',idBacklog)
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

    	
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

    # Eliminar un usuario que no ha sido agregado
    def testdeleteMiembroNotAdded(self):
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
        result = team_object.deleteMiembro('user_not_added','Actor',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')


    #############################################      
    #         Pruebas para getTeam              #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testgetTeam(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor1 = role()
        actor1.insertActor('Actor1','Descripcion',idBacklog)
        result    = actor1.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user1 = user()
        _user1.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el actor 2
        actor2 = role()
        actor2.insertActor('Actor2','Descripcion',idBacklog)
        result    = actor2.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user2 = user()
        _user2.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)
        # Ejecutamos la funcion
        team_object = team()
        team_object.getTeam(idBacklog)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user1.deleteUser('user1')
        actor1.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user2.deleteUser('user2')
        actor2.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Caso en que no hay miembros en el quipo
    def testgetTeamNoMembers(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog
        # Ejecutamos la funcion
        team_object = team()
        result = team_object.getTeam(idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados
        _backlog.deleteProduct('Backlog')

    #############################################      
    #         Pruebas para verifyScrumMaster    #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testverifyScrumMaster(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Actor1',idBacklog) 
        team_object.insertMiembro('user2','Actor2',idBacklog) 
        # Obtenemos los miembros del equipo
        teamList = team_object.getTeam(idBacklog)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':team.EQ_username, 'rol': team.EQ_rol} for team in teamList]
        # Ejecutamos la funcion
        team_object.verifyScrumMaster(lista)
    

if __name__ == '__main__':
    unittest.main()