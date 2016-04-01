# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from sprint import *
from equipo import *

# Declaracion de constantes.
CONST_MAX_NAME_USERNAME = 17
CONST_MIN_NAME_USERNAME = 1
CONST_MIN_ROL = 11
CONST_MAX_ROL = 14


class subEquipoClass(object):
    '''Clase que permite manejar los SubEquipos de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla sub equipo esta vacia'''
        aSubEquipo = clsSubEquipo.query.all()
        return (aSubEquipo == [])

    def getSubEquipo(self,idSprint):
        '''Entrega la lista de miembros de un sub equipo'''

        aSubEquipo = clsSubEquipo.query.filter_by(SEQ_idSprint = idSprint).all()

        return (aSubEquipo)

    def verifyScrumMaster(self,lista):
        cant = 0
        for miembro in lista:
            if miembro['rol'] == "Scrum master":
                cant += 1
        if cant > 1:
                return False
        return True

    def deleteMiembroSubEquipo(self, username, rol,idSprint):
        '''Permite eliminar un miembro de un sub equipo'''
        checkTypeUsername = type(username) == str
        checkTypeRol = type(rol) == str
        checkTypeIdSprint = type(idSprint) == int
        
        if checkTypeUsername and checkTypeRol and checkTypeIdSprint:
            checkLongName = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongRol = CONST_MIN_ROL <= len(rol) <= CONST_MAX_ROL
            checkLongIdSprint = CONST_MIN_ID <= idSprint               
             
            
            if checkLongName and checkLongRol:
                foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint).all()
               
                
                if foundSprint != [] or idSprint == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()
                   

                    if foundUser != []:
                        foundMiembro = clsSubEquipo.query.filter_by(SEQ_username = username,SEQ_idSprint = idSprint).all()
                        
                        if foundMiembro != []:
                            for i in foundMiembro:
                                db.session.delete(i)
                            db.session.commit()
                            #print(self.getSubEquipo(idSprint) == [])
                            return True


        return False 

    def insertMiembroSubEquipo(self,username,rol,idSprint):
        '''Permite insertar un miembro a un sub equipo'''
        
        checkTypeUsername = type(username) == str
        checkTypeRol = type(rol) == str
        checkTypeIdSprint = type(idSprint) == int
        
        if checkTypeUsername and checkTypeRol and checkTypeIdSprint:
            checkLongName = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongRol = CONST_MIN_ROL <= len(rol) <= CONST_MAX_ROL
            checkLongIdSprint = CONST_MIN_ID <= idSprint           
             
            
            if checkLongName and checkLongRol:
                foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint).all()
               
                
                if foundSprint != [] or idSprint == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()
                   

                    if foundUser != []:
                        foundMiembro = clsSubEquipo.query.filter_by(SEQ_username = username,SEQ_idSprint = idSprint).all()                    
                        
                        if foundMiembro == []:
                            newMiembro = clsSubEquipo(username, rol, idSprint)
                            db.session.add(newMiembro)
                            db.session.commit()
                            return True

                        if foundMiembro[0].SEQ_rol != rol:
                            self.deleteMiembroSubEquipo(username,foundMiembro[0].SEQ_rol,idSprint)
                            newMiembro = clsEquipo(username, rol,idSprint)
                            db.session.add(newMiembro)
                            db.session.commit()
                            return True

        return False

    def actualizar(self,lista,idSprint):
        '''Permite actualizar la tabla sub equipo'''
        idPila  = int(session['idPila'])

        users = []
        for elem in lista:
            users += elem['miembro']

        checkTypeId = type(idSprint) == int
        
        if checkTypeId:
            checkLongId = CONST_MIN_ID <= idSprint            
             
            if checkLongId:
                foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint).all()
               
                
                if foundSprint != [] or idSprint == 0:
                    miembros = clsSubEquipo.query.filter_by(SEQ_idSprint = idSprint).all()

                    if self.verifyScrumMaster(lista):
                        for m in miembros:
                            if m.SEQ_username not in users:
                                self.deleteMiembroSubEquipo(m.SEQ_username, m.SEQ_rol,idSprint)

                        for user in lista:
                            username = user['miembro']
                            self.insertMiembroSubEquipo(username,user['rol'],idSprint)

                        if self.getSubEquipo(idSprint) == []:
                            oTeam      = team()
                            teamList = oTeam.getTeamDevs(idPila)
                            for member in teamList:
                                self.insertMiembroSubEquipo(member.EQ_username,member.EQ_rol,idSprint)
                        return True
        return False

# Fin Clase Team