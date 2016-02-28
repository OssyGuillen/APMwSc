# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from flask import session
from backLog import *
from role import *

# Para usar el servicio de verificacion, se importa en el controlador deseado
# y se crea un condicional. Se usa la funcion pasandole como parametro el rol
# necesario para ejecutar la funcion. En caso de pasar la verificacion, se
# ejecuta el request. En caso contrario no procesa el request.

class verifier(object):
	'''Servicio de verificacion de roles'''


	def checkAssignedRole(self, assigned_Role):

		oId_Actor = session['id_Actor']

		return (oId_Actor == assigned_Role)