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
        actor = role()
        actor.insertActor('Actor1','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)
        # Ejecutamos la funcion
        team_object = team()
        team_object.insertMiembro('user1','Actor1',idBacklog)  
        team_object.insertMiembro('user2','Actor2',idBacklog)  
        team_object.getTeam(idBacklog)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Devolver un equipo vacio
    def testgetTeamNone(self):
        # Creamos el backlog
        _backlog_none  = backlog()
        _backlog_none.insertBacklog('Backlog','Prueba',1)
        findId    = _backlog_none.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el objeto
        borrar_objeto = clsEquipo.query.filter_by(EQ_rol='Desarrollador')
        for objeto in borrar_objeto:
            db.session.delete(objeto)
        team_object_none = team()
        result = team_object_none.getTeam(idBacklog)
        self.assertEqual(result,[])
        # Eliminamos los datos insertados
        _backlog_none.deleteProduct('Backlog')


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
        actor.insertActor('Actor1','Desarrollador',idBacklog)
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
         # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Probar que no puede haber mas de un Scrum master
    def testverifyScrumMasterFalse(self):
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
        team_object.insertMiembro('user1','Scrum master',idBacklog) 
        team_object.insertMiembro('user2','Scrum master',idBacklog) 
        # Obtenemos los miembros del equipo
        teamList = team_object.getTeam(idBacklog)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':team.EQ_username, 'rol': team.EQ_rol} for team in teamList]
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertFalse(result)
         # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Ningun miembro es Scrum master
    def testverifyScrumMasterNone(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Obtenemos los miembros del equipo
        teamList = team_object.getTeam(idBacklog)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':team.EQ_username, 'rol': team.EQ_rol} for team in teamList]
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertTrue(result)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    #############################################      
    #         Pruebas para actualizar           #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testActualizar(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 3
        actor.insertActor('Actor3','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor3',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)
        # Creamos el usuario 3
        _user.insertUser('fullname','user3','password1233','prueba@user3.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Obtenemos los miembros del equipo
        teamList = team_object.getTeam(idBacklog)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':team.EQ_username, 'rol': team.EQ_rol} for team in teamList]
        team_object.insertMiembro('user3','Scrum master',idBacklog) 
        team_object.actualizar(lista,idBacklog)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        team_object.deleteMiembro('user3','Actor3',idBacklog)
        _user.deleteUser('user3')
        actor.deleteActor('Actor3',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Los miembros que se actualizan son los mismos de la base de datos
    def testActualizarSame(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Obtenemos los miembros del equipo
        teamList = team_object.getTeam(idBacklog)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':team.EQ_username, 'rol': team.EQ_rol} for team in teamList]
        team_object.actualizar(lista,idBacklog)
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertTrue(result)
        # Eliminamos los datos insertados
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')


if __name__ == '__main__':
    unittest.main()