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
    #         Pruebas para insertArchivo        #
    #############################################

    # Caso inicial
    #Verificar que el archivo se pueda cargar con el nombre correspondiente
    # Prueba 1
    def testInsertArchivoExist(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos Normales
    #Verificar que el archivo se pueda cargar con el nombre correspondiente
    # Prueba 2
    def testInsertArchivoElement(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos fronteras
    #Archivo posee Mayuscula
    # Prueba 3
    def testInsertArchivoElementMay(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
    #Archivo posee minusculas
    # Prueba 4
    def testInsertArchivoElementMin(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    #Archivo posee digitos
    # Prueba 5
    def testInsertArchivoElementDigits(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('1234','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('1234')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    #Archivo posee combinacion de todas las anteriores
    # Prueba 6
    def testInsertArchivoElementCombinational(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('VtXcyr123','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('VtXcyr123')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    #Archivo de 20 caracteres de largo
    # Prueba 7
    def testInsertArchivoElement20Long(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive(20*'V','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName(20*'V')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos esquina
    #Sin Backlog
    # Prueba 8
    def testInsertArchivoElementSinBacklog(self):
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), [], 'ASSASAS')
        self.assertFalse(result)
        # Eliminamos los datos insertados.

    #nombre de 50 o mas sin Backlog
    # Prueba 9
    def testInsertArchivoElement50Chars(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive(50*'V','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName(50*'V')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos maliciosos
    #Simbolos que representan PATH en nuestro SO
    # Prueba 10
    def testInsertArchivoElementPathSym(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        result = aArchive.insertArchive('../','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive1 = aArchive.findName('../')
        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
    #Archivo nombre vacio
    # Prueba 11
#    def testInsertArchivoEmptyName(self):
#        # Insertamos los datos necesarios.
#        aBacklog  = backlog()
#        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
#        findId    = aBacklog.findName('Bxtyllz')
#        idBacklog = findId[0].BL_idBacklog
#        # Inicio de la prueba.
#        aArchive      = archivos()
#        result = aArchive.insertArchive('','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
#        self.assertFalse(result)
#        # Eliminamos los datos insertados.
#        aArchive1 = aArchive.findName('')
#        aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
#        aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #         Pruebas para searchArchivo        #
    #############################################

    # Caso inicial
    # Busqueda exitosa
    # Prueba 11
    def testFindIsArchive(self):
       # Insertamos los datos necesarios.
       aBacklog  = backlog()
       aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
       findId    = aBacklog.findName('Bxtyllz')
       idBacklog = findId[0].BL_idBacklog
       # Inicio de la prueba.
       aArchive      = archivos()
       aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
       aArchive1 = aArchive.findName('VtXcyr')
       result = aArchive.findIdArchives(aArchive1[0].AR_idArchivos)
       self.assertTrue(result)
       # Eliminamos los datos insertados.
       aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
       aBacklog.deleteProduct('Bxtyllz')

    # Casos normales
    #Si el archivo existe
    # Prueba 12
    def testFindIsArchiveExist(self):
       # Insertamos los datos necesarios.
       aBacklog  = backlog()
       aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
       findId    = aBacklog.findName('Bxtyllz')
       idBacklog = findId[0].BL_idBacklog
       # Inicio de la prueba.
       aArchive      = archivos()
       aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
       aArchive1 = aArchive.findName('VtXcyr')
       result = aArchive.findIdArchives(aArchive1[0].AR_idArchivos)
       self.assertTrue(result)
       # Eliminamos los datos insertados.
       aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
       aBacklog.deleteProduct('Bxtyllz')

    #Si el archivo no existe
    # Prueba 13
    def testFindIsArchiveNotExist(self):
       # Insertamos los datos necesarios.
       aBacklog  = backlog()
       aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
       findId    = aBacklog.findName('Bxtyllz')
       idBacklog = findId[0].BL_idBacklog
       # Inicio de la prueba.
       aArchive      = archivos()
       result = aArchive.findIdArchives(1)
       self.assertFalse(result)
       # Eliminamos los datos insertados.
       aBacklog.deleteProduct('Bxtyllz')

    # Casos maliciosos
    #El Id del archivo es invalido
    # Prueba 14
    def testFindIsArchiveInvalid(self):
       # Insertamos los datos necesarios.
       aBacklog  = backlog()
       aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
       findId    = aBacklog.findName('Bxtyllz')
       idBacklog = findId[0].BL_idBacklog
       # Inicio de la prueba.
       aArchive      = archivos()
       result = aArchive.findIdArchives("a")
       self.assertFalse(result)
       # Eliminamos los datos insertados.
       aBacklog.deleteProduct('Bxtyllz')


    #Valor del Id negativo
    # Prueba 15
    # Insertamos los datos necesarios.
    def testFindIsArchiveNegative(self):
       # Insertamos los datos necesarios.
       aBacklog  = backlog()
       aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
       findId    = aBacklog.findName('Bxtyllz')
       idBacklog = findId[0].BL_idBacklog
       # Inicio de la prueba.
       aArchive      = archivos()
       result = aArchive.findIdArchives(-1)
       self.assertFalse(result)
       # Eliminamos los datos insertados.
       aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #         Pruebas para deleteArchivo        #
    #############################################

    # Caso inicial
    # Prueba 16
    def testDeleteArchivo(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')

        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Casos Normales
    # El archivo existe y se borra exitosamente
    # Prueba 17
    def testDeleteArchivoNormal(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Casos Esquinas
    # Prueba 18

    def testDeleteArchivoEsquina(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive(50*'A','/foo/bar/baz', datetime.datetime.now(), idBacklog,'ASSASASC')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 19
    def testDeleteArchivoEsquina(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr',200*'B', datetime.datetime.now(), idBacklog, 'ASSASASC')

        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 20
    def testDeleteArchivoEsquina(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 50*'C')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)


    # Casos fronteras
    # Longuitud de archivo (grande y pequeña)
    # Prueba 21
    def testDeleteArchivoShortTag1(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog,'A')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 22
    def testDeleteArchiveShortTag100(self):
         # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog,100*'A')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 23
    def testDeleteArchiveShortName1(self):
         # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('V','/foo/bar/baz', datetime.datetime.now(), idBacklog,'Axsdf')
        #probamos borrar
        aArchive1 = aArchive.findName('V')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 24
    def testDeleteArchiveShortName50(self):
         # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive(50*'V','/foo/bar/baz', datetime.datetime.now(), idBacklog,'Axsdf')
        #probamos borrar
        aArchive1 = aArchive.findName(50*'V')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 25
    def testDeleteArchiveShortUrl1(self):
         # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','f', datetime.datetime.now(), idBacklog,'Axsdf')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    # Prueba 26
    def testDeleteArchiveShortUrl200(self):
         # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog

         # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr',200*'f', datetime.datetime.now(), idBacklog,'Axsdf')
        #probamos borrar
        aArchive1 = aArchive.findName('VtXcyr')
        result = aArchive.deleteArchive(aArchive1[0].AR_idArchivos)
        aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)


#if __name__ == '__main__':
    #unittest.main()

