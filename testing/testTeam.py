# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from Team import *

class TestTeam(unittest.TestCase):
	
	#############################################      
    #         Pruebas para emptyTable           #
    #############################################

    def testEmptyTable(self):
    	# Probar que la funcionalidad se ejecuta
    	team_object = team()
    	team_object.emptyTable()
    	

    	
if __name__ == '__main__':
    unittest.main()