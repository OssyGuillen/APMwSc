# -*- coding: utf-8 -*-. 
 
import sys
import unittest

#Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog				import *
from actorsUserHistory		import *
from userHistory			import *
from accions				import *   
from model				  	import *  
from task				   	import *
from category				import *
from precedence				import *

class TestPrecedence (unittest.TestCase):

	#########################
	#   INSERT PRECEDENCE   #
	#########################

	#Prueba 1
	def testInsertPrecedenceExists(self):
		# Insertamos Producto
		aBacklog = backlog()
		aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
		searchBacklog = aBacklog.findName('Podn fjdd.')
		idFound0 = searchBacklog[0].BL_idBacklog
	 
		# Insertamos la accion
		aAcc = accions()
		aAcc.insertAccion('cinrohbwidia',idFound0)
		search = aAcc.searchAccion('cinrohbwidia',idFound0)
		idFound = search[0].AC_idAccion
			   
		# Insertamos la historia
		aHist = userHistory()
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1.HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2.HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idesegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

