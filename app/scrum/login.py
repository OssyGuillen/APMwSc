# -*- coding: utf-8 -*-

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from   model import *
import uuid
import hashlib
import re

class login(object):
    '''Permite manejar la seguridad de una clave'''
    
    def __init__(self):
        ohast=''
        self.expressionRegular = ('(([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*)|'
                                  '(([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*)|'
                                  '(([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*)|'
                                  '(([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*)|'
                                  '(([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*)|'
                                  '(([a-z]|[A-Z]|\d|[@.#$+*])*\d([a-z]|[A-Z]|\d|[@.#$+*])*[A-Z]([a-z]|[A-Z]|\d|[@.#$+*])*[@.#$+*]([a-z]|[A-Z]|\d|[@.#$+*])*)')
   
    def validPassword(self, password):
        olength_password=self.length_password(password) 
               
        if olength_password>=8 and olength_password<=16:
            validPassword = re.search(self.expressionRegular,password)
             
            if validPassword:
                return True
            else:
                return False
            

    def encript(self, value):
        '''Permite encriptar una clave dada'''
        oHash = ""
        # Verificar la longitud del password
        olength_password=self.length_password(value)
        
        if olength_password>=8 and olength_password<=16:
            validPassword= re.search(self.expressionRegular, value)
            
            if validPassword:
                # uuid es usado para generar numeros random
                salt = uuid.uuid4().hex
                # hash
                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
                return oHash
            else:
                return oHash
        else:
            return oHash  
         
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        '''Permite comprobar si una clave encriptada corresponde a una clave dada'''
        # Verificar la longitud del password
        olength_password=self.length_password(oCheckPassword) 
               
        if olength_password>=8 and olength_password<=16:
            validPassword= re.search(self.expressionRegular,oCheckPassword) 
            
            if validPassword:
                oPassworkEncript, salt = oPassworkEncript.split(':')
                return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
            else:
                return False
        else:
            return False
        
    
    def length_password(self, user_password):
        '''Permite verificar el tamano de un password'''
        return len(user_password)
