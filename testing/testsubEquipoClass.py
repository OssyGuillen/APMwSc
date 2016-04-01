# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo subEquipoClass.py
sys.path.append('../app/scrum')

from sprint import *
from equipo import *

class TestsubEquipoClass(unittest.TestCase):
	#############################################      
    #         Pruebas para emptyTable           #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testEmptyTable(self):
        subequipo_object = subEquipoClass()
        subequipo_object.emptyTable()

    # Probar que hay elementos en subEquipo
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
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog)
        # Agregamos un usuario a team
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)
        # Agregamos el usuario al subEquipo
        subequipo_object.insertMiembroSubEquipo('userr','Actor',1)
        # Ejecutamos la funcion
        result = subequipo_object.emptyTable()
        self.assertFalse(result)
        # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('userr','Actor',1)
        team_object.deleteMiembro('userr','Actor',idBacklog)
        aSprint.deleteSprint(1,idBacklog)
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

if __name__ == '__main__':
    unittest.main()