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
    #         Pruebas para VAsignacionTarea        #
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

#if __name__ == '__main__':
    #unittest.main()

