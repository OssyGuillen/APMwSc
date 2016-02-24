# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes.
CONST_MAX_NAME_USERNAME = 17
CONST_MIN_NAME_USERNAME = 1
CONST_MIN_ROL = 11
CONST_MAX_ROL = 14


class team(object):
    '''Clase que permite manejar los Equipos de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla equipo esta vacia'''
        aTeam = clsEquipo.query.all()
        return (aTeam == [])

    def getTeam(self,idBacklog):
        '''Entrega la lista de miembros de un equipo'''

        aTeam = clsEquipo.query.filter_by(EQ_idBacklog = idBacklog).all()

        return (aTeam)

    def deleteMiembro(self, username, rol,idBacklog):
        '''Permite eliminar un miembro de un equipo'''
        
        checkTypeUsername = type(username) == str
        checkTypeRol = type(rol) == str
        checkTypeId = type(idBacklog) == int
        
        if checkTypeUsername and checkTypeRol and checkTypeId:
            checkLongName = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongRol = CONST_MIN_ROL <= len(rol) <= CONST_MAX_ROL
            checkLongId = CONST_MIN_ID <= idBacklog            
             
            
            if checkLongName and checkLongRol:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
               
                
                if foundBacklog != [] or idBacklog == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()
                   

                    if foundUser != []:
                        foundMiembro = clsEquipo.query.filter_by(EQ_username = username, EQ_idBacklog = idBacklog).all()
                        
                        if foundMiembro != []:
                            for i in foundMiembro:    
                                db.session.delete(i)          
                            db.session.commit()
                            return True


        return False 

    def insertMiembro(self,username,rol,idBacklog):
        '''Permite insertar un miembro a un equipo'''
        
        checkTypeUsername = type(username) == str
        checkTypeRol = type(rol) == str
        checkTypeId = type(idBacklog) == int
        
        if checkTypeUsername and checkTypeRol and checkTypeId:
            checkLongName = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongRol = CONST_MIN_ROL <= len(rol) <= CONST_MAX_ROL
            checkLongId = CONST_MIN_ID <= idBacklog            
             
            
            if checkLongName and checkLongRol:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
               
                
                if foundBacklog != [] or idBacklog == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()
                   

                    if foundUser != []:
                        foundMiembro = clsEquipo.query.filter_by(EQ_username = username, EQ_idBacklog = idBacklog).all()                       
                        
                        if foundMiembro == []:
                            newMiembro = clsEquipo(username, rol, idBacklog)
                            db.session.add(newMiembro)
                            db.session.commit()
                            return True

                        if foundMiembro[0].EQ_rol != rol:
                            self.deleteMiembro(username,foundMiembro[0].EQ_rol,idBacklog)
                            newMiembro = clsEquipo(username, rol, idBacklog)
                            db.session.add(newMiembro)
                            db.session.commit()
                            return True

        return False

    def actualizar(self,lista,idBacklog):
        '''Permite actualizar la tabla equipo'''
        users = []
        for elem in lista:
            users += elem['miembro']

        checkTypeId = type(idBacklog) == int
        
        if checkTypeId:
            checkLongId = CONST_MIN_ID <= idBacklog            
             
            if checkLongId:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
               
                
                if foundBacklog != [] or idBacklog == 0:
                    miembros = clsEquipo.query.filter_by(EQ_idBacklog = idBacklog).all()
                    for miembro in miembros:
                        if miembro.EQ_username not in users:
                            self.deleteMiembro(miembro.EQ_username, miembro.EQ_rol, idBacklog)

                    for user in lista:
                        username = user['miembro']
                        self.insertMiembro(username,user['rol'],idBacklog)
                    return True
        return False

# Fin Clase Team