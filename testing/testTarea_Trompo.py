# -*- coding: utf-8 -*-.

import sys
import unittest
from datetime import datetime

# Ruta que permite utilizar el módulo anexo.py
sys.path.append('../app/scrum')

from model import *
from backLog import *
from archivos import *



class TestArchivo(unittest.TestCase):


    #############################################
    #         Pruebas para VAsignacionTarea     #
    #############################################

    # Caso inicial
    #Verificar que la persona a asignar pertenece a la lista de actores
    # Prueba 1
    def testVAsignacionTareaExist(self):
       idTarea = request.args['idTarea']
       res = {}
       if "actor" in session:
           res['actor']=session['actor']
       result = VAsignacionTarea(idTarea)
       self.assertTrue(result)

    # Casos Normales
    #Verificar que la persona a asignar no pertenece a la lista de actores
    # Prueba 2
    def testVAsignacionTareaNotExist(self):
       idTarea = request.args['idTarea']
       res = {}
       if 'usuario' not in session:
           res['logout'] = '/'
           return json.dumps(res)
       result = VAsignacionTarea(idTarea)
       self.assertFalse(result)


    #############################################
    #  Pruebas para AActualizarAsignacionTarea  #
    #############################################

    # Caso inicial
    #Verificar que la actualizacion a asignar se lleve a cabo de manera correcta
    # Prueba 3
    # params = request.get_json()
    # results = [{'label':'/VAsignacionTarea', 'msg':['Asignación actualizada']}, {'label':'/VAsignacionTarea', 'msg':['Error al actualizar la asignacion de la tarea']}, ]
    # res = results[0]
    # #Inicio de la Prueba
    # idTarea  = int(session['idTarea'])
    # idTarea2  = int(session['idTarea2'])
    # res['label'] = res['label'] + '/' + str(idTarea)
    # c = task()
    # c.insertUserTask(idTarea, 4)
    # c.insertUserTask(idTarea2, 3)
    # VAsignacionTarea(idTarea)
    # result = AActualizarAsignacionTarea(idTarea2)
    # self.assertTrue(result)
    
    # # Caso Normal
    # #Verificar que la actualizacion de cambiar la asignacion al mismo usuario
    # # Prueba 4
    # params = request.get_json()
    # results = [{'label':'/VAsignacionTarea', 'msg':['Asignación actualizada']}, {'label':'/VAsignacionTarea', 'msg':['Error al actualizar la asignacion de la tarea']}, ]
    # res = results[0]
    # #Inicio de la Prueba
    # idTarea  = int(session['idTarea'])
    # res['label'] = res['label'] + '/' + str(idTarea)
    # c = task()
    # c.insertUserTask(idTarea, 4)
    # VAsignacionTarea(idTarea)
    # result = AActualizarAsignacionTarea(idTarea)
    # self.assertTrue(result)
    
    # # Caso por Malicia
    # #Verificar que la actualizacion de cambiar la asignacion a un usuario nulo
    # # Prueba 5
    # params = request.get_json()
    # results = [{'label':'/VAsignacionTarea', 'msg':['Asignación actualizada']}, {'label':'/VAsignacionTarea', 'msg':['Error al actualizar la asignacion de la tarea']}, ]
    # res = results[0]
    # #Inicio de la Prueba
    # idTarea  = int(session['idTarea'])
    # idTarea2  = int(session[None])
    # res['label'] = res['label'] + '/' + str(idTarea)
    # c = task()
    # c.insertUserTask(idTarea, 1)
    # VAsignacionTarea(idTarea)
    # result = AActualizarAsignacionTarea(idTarea2)
    # self.assertFalse(result)
 
    

#if __name__ == '__main__':
    #unittest.main()

