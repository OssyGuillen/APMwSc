# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from login import *

class TestLogin(unittest.TestCase):
        
    ##########################################      
    #        Pruebas para encript            #
    ##########################################
    
    # Caso Inicial
    
    # Prueba 1
    def testEncriptExists(self):
        oLogin = login()
        oHash  = oLogin.encript("Asj123.")
        
    # Casos Frontera
     
    #Prueba 2
    def testEncriptLengthEightValidString(self): 
        oLogin = login() 
        oHash  = oLogin.encript("pa$$w0rD") # longitud 8    caracteres validos
        self.assertNotEqual("",oHash)
         
    # Prueba 3
    def testEncriptLengthSixteenValidString(self):    
        oLogin = login() 
        oHash  = oLogin.encript("16.9rh@Ag5wxQzp0") # longitud 16    caracteres validos
        self.assertNotEqual("",oHash)   
         
    # Prueba 4
    def testEncriptLengthNineValidString(self):    
        oLogin = login() 
        oHash  = oLogin.encript("pa$$w0rD.") # longitud 9    caracteres validos      
        self.assertNotEqual("",oHash)
         
    # Prueba 5
    def testEncriptLengthFifteenValidString(self):  
        oLogin = login() 
        oHash  = oLogin.encript("16.9rh@AgwxQzp0") # longitud 15    caracteres validos
        self.assertNotEqual("",oHash)
        
    # Casos Esquina
    
    # Prueba 6
    def testEncriptLengthEightInvalidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("_ko8E{?}")  # longitud 8    caracteres invalidos
        self.assertEqual("",oHash)
       
    # Prueba 7
    def testEncriptLengthEightNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpeWr@") # longitud 8    sin digitos
        self.assertEqual("",oHash)

    # Prueba 8
    def testEncriptLengthEightNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("$s@kp.f*") # longitud 8    sin digitos ni mayusculas
        self.assertEqual("",oHash)

    # Prueba 9
    def testEncriptLengthEightNotDigitsNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("fToesQhp") # longitud 8    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)

    # Prueba 10
    def testEncriptLengthEightNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("d#6fo@.3") # longitud 8    sin mayusculas
        self.assertEqual("",oHash)

    # Prueba 11
    def testEncriptLengthEightNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("irj1290k") # longitud 8    sin mayusculas ni caracteres especiales
        self.assertEqual("",oHash)
      
    # Prueba 12 
    def testEncriptLengthEightNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("1F09irA2") # longitud 8    sin caracteres especiales
        self.assertEqual("",oHash)
              
    # Prueba 13          
    def testEncriptLengthSixteenInvalidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("_k?¡[ñ]<z]>o8E{}") # longitud 16    caracteres invalidos
        self.assertEqual("",oHash)
    
    # Prueba 14     
    def testEncriptLengthSixteenNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpeWo@lEdff@#*") # longitud 16    sin digitos
        self.assertEqual("",oHash)
         
    # Prueba 15
    def testEncriptLengthSixteenNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("$s@kpf#.*rthq+f*") # longitud 16    sin digitos ni mayusculas
        self.assertEqual("",oHash)
    
    # Prueba 16     
    def testEncriptLengthSixteenNotDigitsNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("fToesQpUGndpwder") # longitud 16    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)
         
    # Prueba 17
    def testEncriptLengthSixteenNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("d#6fo@3$.+*t34do") # longitud 16    sin mayusculas
        self.assertEqual("",oHash)
         
    # Prueba 18
    def testEncriptLengthSixteenNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("irj120k720fnsl0j") # longitud 16    sin mayusculas ni caracteres especiales
        self.assertEqual("",oHash)
         
    # Prueba 19
    def testEncriptLengthSixteenNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("1F09ir2UNdpw3450") # longitud 16    sin caracteres especiales
        self.assertEqual("",oHash)
                        
    # Casos Normales
    
    # Prueba 20
    def testEncriptLengthNineInvalidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("_ko8E{?}¬") # longitud 9    caracteres invalidos
        self.assertEqual("",oHash)
    
    # Prueba 21     
    def testEncriptLengthNineNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpeWr@t") # longitud 9    sin digitos
        self.assertEqual("",oHash)
    
    # Prueba 22
    def testEncriptLengthNineNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("$s@kp.f*p") # longitud 9    sin digitos ni mayusculas
        self.assertEqual("",oHash)
    
    # Prueba 23     
    def testEncriptLengthNineNotDigitsNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("fToesQhpI") # longitud 9    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)
        
    # Prueba 24
    def testEncriptLengthNineNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("d#6fo@.3q") # longitud 9    sin mayusculas
        self.assertEqual("",oHash)
        
    # Prueba 25
    def testEncriptLengthNineNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("irj1290k1") # longitud 9    sin mayusculas ni caracteres especiales
        self.assertEqual("",oHash)
    
    # Prueba 26
    def testEncriptLengthNineNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("1F09irA20") # longitud 9    sin caracteres especiales
        self.assertEqual("",oHash)
    
    # Prueba 27
    def testEncriptLengthNineNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("fpeosrnql") # longitud 9    sin los requisitos minimos
        self.assertEqual("",oHash)
        
    # Prueba 28
    def testEncriptLengthFifteenInvalidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("_k?¡[ñ]<z]o8E{}") # longitud 15    caracteres invalidos
        self.assertEqual("",oHash)
         
    # Prueba 29
    def testEncriptLengthFifteenNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpWo@lEdff@#*") # longitud 15    sin digitos
        self.assertEqual("",oHash)
         
    # Prueba 30
    def testEncriptLengthFifteenNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("$s@kp#.*rthq+f*") # longitud 15    sin digitos ni mayusculas
        self.assertEqual("",oHash)
    
    # Prueba 31     
    def testEncriptLengthFifteenNotDigitsNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("fToesQpUGndpder") # longitud 15    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)
    
    # Prueba 32
    def testEncriptLengthFifteenNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("d#6o@3$.+*t34do") # longitud 15    sin mayusculas
        self.assertEqual("",oHash) 
         
    # Prueba 33
    def testEncriptLengthFifteenNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("ir120k720fnsl0j") # longitud 15    sin mayusculas ni caracteres especiales
        self.assertEqual("",oHash)

    # Prueba 34
    def testEncriptLengthFifteenNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("1F09ir2UNdpw350") # longitud 15    sin caracteres especiales
        self.assertEqual("",oHash)
        
    # Prueba 35
    def testEncriptLengthFifteenNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("fpeosnqjdengosq") # longitud 15    sin los requisitos minimos
        self.assertEqual("",oHash)
        
    # Casos Malicia
    
    # Prueba 36
    def testEncriptLengthZero(self):
        oLogin = login()
        oHash  = oLogin.encript("") # Longitud 0
        self.assertEqual("",oHash)
        
    # Prueba 37
    def testEncriptLengthSevenNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("fpeosnq") # longitud 7    sin los requisitos minimos
        self.assertEqual("",oHash)
        
    # Prueba 38
    def testEncriptLengthEightNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("fpeosrnq") # longitud 8    sin los requisitos minimos
        self.assertEqual("",oHash)
    
    # Prueba 39
    def testEncriptLengthSixteenNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("fpeosnqjdoengosq") # longitud 16    sin los requisitos minimos
        self.assertEqual("",oHash)

    # Prueba 40
    def testEncriptLengthSeventeenNoMinimumRequirements(self):
        oLogin = login() 
        oHash  = oLogin.encript("00000000000000000") # longitud 17    sin los requisitos minimos 
        self.assertEqual("",oHash)
       
    # Prueba 41
    def testEncriptLengthSevenValidString(self):
        oLogin = login() 
        oHash  = oLogin.encript("M3A0$d8") # longitud 7    caracteres validos
        self.assertEqual("",oHash)
        
    # Prueba 42
    def testEncriptLengthSevenInvalidString(self):
        oLogin = login() 
        oHash  = oLogin.encript("_ko8E{}") # longitud 7    caracteres invalidos
        self.assertEqual("",oHash)
        
    # Prueba 43
    def testEncriptLengthSevenNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpeW@") # longitud 7   sin digitos
        self.assertEqual("",oHash)
        
    # Prueba 44
    def testEncriptLengthSevenNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("$s@kpf*") # longitud 7    sin digitos ni mayusculas
        self.assertEqual("",oHash)
        
    # Prueba 45
    def testEncriptLengthSevenNotDigitsNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("fToesQp") # longitud 7    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)
        
    # Prueba 46
    def testEncriptLengthSevenNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("d#6fo@3") # longitud 7    sin mayusculas
        self.assertEqual("",oHash)
        
    # Prueba 47
    def testEncriptLengthNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("irj120k") # longitud 7    sin mayusculas ni caracteres especiales
        self.assertEqual("", oHash)
         
    # Prueba 48
    def testEncriptLengthNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("1F09ir2") # longitud 7    sin caracteres especiales
        self.assertEqual("",oHash)     
        
    # Prueba 49
    def testEncriptLengthSeventeenValidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("C*@d$.3Aca#a3aE+$") # longitud 17    caracteres validos
        self.assertEqual("",oHash)
         
    # Prueba 50
    def testEncriptLengthSeventeenInvalidCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("(-:cpsm09JK\?|{=]") # longitud 17    caracteres invalidos   
        self.assertEqual("",oHash)
         
    # Prueba 51
    def testEncriptLengthSeventeenNotDigits(self):
        oLogin = login() 
        oHash  = oLogin.encript("#.LpeW@+lnkzA.@yl") # longitud 17    sin digitos
        self.assertEqual("",oHash)
         
    # Prueba 52
    def testEncriptLengthSeventeenNotDigitsNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("k*sdj+fwei..weh@#") # longitud 17    sin digitos ni mayusculas
        self.assertEqual("",oHash)
      
    # Prueba 53
    def testEncriptLengthSeventeenNotDigitsNotSpecialCharacters(self):  
        oLogin = login() 
        oHash  = oLogin.encript("MJiqJwieALniDGRou") # longitud 17    sin digitos ni caracteres especiales
        self.assertEqual("",oHash)
         
    # Prueba 54
    def testEncriptLengthSeventeenNotCapitalized(self):
        oLogin = login() 
        oHash  = oLogin.encript("@#$+zj*ic71c22x..") # longitud 17    sin mayusculas
        self.assertEqual("",oHash)
         
    # Prueba 55
    def testEncriptLengthSeventeenNotCapitalizedNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("i3u48712384uioiqm") # longitud 17    sin mayusculas ni caracteres especiales
        self.assertEqual("",oHash)
         
    # Prueba 56
    def testEncriptLengthSeventeenNotSpecialCharacters(self):
        oLogin = login() 
        oHash  = oLogin.encript("JFFefn93kNJK43672") # longitud 17    sin caracteres especiales
        self.assertEqual("",oHash)      
           
        
    ##########################################      
    #      Pruebas para check_password       #
    ##########################################
         
    # Caso Inicial

    # Prueba 57
    def testCheck_passwordExists(self):
        oLogin           = login()
        message          = "Asj123."
        encriptedMessage = oLogin.encript(message)
        oLogin.check_password(encriptedMessage,message)
        
    # Casos Frontera
    
    # Prueba 58
    def testCheck_passwordLengthSevenValidCharacters(self):
        oLogin           = login() 
        message          = "M3A0$d8"  # Longitud 7    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 59
    def testCheck_passwordLengthEightValidCharacters(self):
        oLogin           = login() 
        message          = "pa$$w0rD"  # longitud 8    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertTrue(result)

    # Prueba 60
    def testCheck_passwordLengthSixteenValidCharacters(self):
        oLogin           = login() 
        message          = "16.9rh@Ag5wxQzp0"  # longitud 16    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertTrue(result)
        
    # Prueba 61
    def testCheck_passwordLengthSeventeenValidCharacters(self):
        oLogin           = login() 
        message          = "C*@d$.3Aca#a3aE+$"    # longitud 17    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
                
    # Casos Normales
    
    # Prueba 62
    def testCheck_passwordLengthNineValidCharacters(self):
        oLogin           = login() 
        message          = "pa$$w0rD."  # longitud 9    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertTrue(result)
        
    # Prueba 63
    def testCheck_passwordLengthNineInvalidCharacters(self):
        oLogin           = login() 
        message          = "_ko8E{?}Â¬"  # longitud 9    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
         
    # Prueba 64
    def testCheck_passwordLengthNineNotDigits(self):
        oLogin           = login() 
        message          = "#.LpeWr@t"  # longitud 9    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
         
    # Prueba 65
    def testCheck_passwordLengthNineNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "$s@kp.f*p"  # longitud 9    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
               
    # Prueba 66
    def testCheck_passwordLengthNineNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "fToesQhpI"  #longitud 9    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
            
    # Prueba 67
    def testCheck_passwordLengthNineNotCapitalized(self): 
        oLogin           = login() 
        message          = "d#6fo@.3q"  #longitud 9    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
       
    # Prueba 68
    def testCheck_passwordLengthNineNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "irj1290k1"  #longitud 9    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
             
    # Prueba 69
    def testCheck_passwordLengthNineNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "1F09irA20"  #longitud 9    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 70
    def testCheck_passwordLengthNineNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "fpeosrnql"  #longitud 9    sin los requisitos minimos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
            
    # Prueba 71
    def testCheck_passwordLengthFifteenValidCharacters(self):
        oLogin           = login() 
        message          = "16.9rh@AgwxQzp0"  # longitud 15    caracteres validos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertTrue(result)
        
    # Prueba 72
    def testCheck_passwordLengthFifteenInvalidCharacters(self):
        oLogin           = login() 
        message          = "_k?Â¡[Ã±]<z]o8E{}"  # longitud 15    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
    
    # Prueba 73
    def testCheck_passwordLengthFifteenNotDigits(self):
        oLogin           = login() 
        message          = "#.LpWo@lEdff@#*"  # longitud 15    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 74
    def testCheck_passwordLengthFifteenNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "$s@kp#.*rthq+f*"  # longitud 15    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 75
    def testCheck_passwordLengthFifteenNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "fToesQpUGndpder"  #longitud 15    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
      
    # Prueba 76
    def testCheck_passwordLengthFifteenNotCapitalized(self): 
        oLogin           = login() 
        message          = "d#6o@3$.+*t34do"  #longitud 15    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 77
    def testCheck_passwordLengthFifteenNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "ir120k720fnsl0j"  #longitud 15    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
    
    # Prueba 78
    def testCheck_passwordLengthFifteenNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "1F09ir2UNdpw350"  #longitud 15    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 79
    def testCheck_passwordLengthFifteenNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "fpeosnqjdengosq"  #longitud 15    sin los requisitos minimos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Casos Esquina
        
    # Prueba 80
    def testCheck_passwordLengthEightInvalidCharacters(self):
        oLogin           = login() 
        message          = "_ko8E{?}"  # longitud 8    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)     
        
    # Prueba 81
    def testCheck_passwordLengthEightNotDigits(self):
        oLogin           = login() 
        message          = "#.LpeWr@"  # longitud 8    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 82
    def testCheck_passwordLengthEightNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "$s@kp.f*"  # longitud 8    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 83
    def testCheck_passwordLengthEightNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "fToesQhp"  # longitud 8    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)       
        
    # Prueba 84
    def testCheck_passwordLengthEightNotCapitalized(self): 
        oLogin           = login() 
        message          = "d#6fo@.3"  # longitud 8    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 85
    def testCheck_passwordLengthEightNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "irj1290k"  # longitud 8    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
                 
    # Prueba 86
    def testCheck_passwordLengthEightNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "1F09irA2"  # longitud 8    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
    
    # Prueba 87
    def testCheck_passwordLengthSixteenInvalidCharacters(self):
        oLogin           = login() 
        message          = "_k?Â¡[Ã±]<z]>o8E{}"  # longitud 16    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
             
    # Prueba 88
    def testCheck_passwordLengthSixteenNotDigits(self):
        oLogin           = login() 
        message          = "#.LpeWo@lEdff@#*"  # longitud 16    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
          
    # Prueba 89
    def testCheck_passwordLengthSixteenNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "$s@kpf#.*rthq+f*"  # longitud 16    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 90
    def testCheck_passwordLengthSixteenNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "fToesQpUGndpwder"  # longitud 16    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
      
    # Prueba 91
    def testCheck_passwordLengthSixteenNotCapitalized(self): 
        oLogin           = login() 
        message          = "d#6fo@3$.+*t34do"  # longitud 16    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
      
    # Prueba 92
    def testCheck_passwordLengthSixteenNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "irj120k720fnsl0j"  # longitud 16    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
                 
    # Prueba 93
    def testCheck_passwordLengthSixteenNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "1F09ir2UNdpw3450"  # longitud 16    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)    
        
    # Casos Malicia
    
    # Prueba 94
    def testCheck_passwordLengthZero(self):
        oLogin           = login() 
        message          = ""
        encriptedMessage = oLogin.encript(message) # longitud 0
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 95
    def testCheck_passwordLengthSevenNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "fpeosnq"  # longitud 7    sin los requisitos minimos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 96
    def testCheck_passwordLengthEightNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "fpeosrnq"  # longitud 8    sin los requisitos minimos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 97
    def testCheck_passwordLengthSixteenNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "fpeosnqjdoengosq"  # longitud 16    sin los requisitos minimos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 98
    def testCheck_passwordLengthSeventeenNoMinimumRequirements(self):
        oLogin           = login() 
        message          = "00000000000000000"    # longitud 17    sin los requisitos minimos    
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)    
        
    # Prueba 99
    def testCheck_passwordLengthSevenInvalidCharacters(self):
        oLogin           = login() 
        message          = "_ko8E{}"  # longitud 7    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 100
    def testCheck_passwordLengthSevenNotDigits(self):
        oLogin           = login() 
        message          = "#.LpeW@"  # longitud 7    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 101
    def testCheck_passwordLengthSevenNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "$s@kpf*"  # longitud 7    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 102
    def testCheck_passwordLengthSevenNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "fToesQp"  # longitud 7    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 103
    def testCheck_passwordLengthSevenNotCapitalized(self): 
        oLogin           = login() 
        message          = "d#6fo@3"  # longitud 7    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 104
    def testCheck_passwordLengthSevenNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "irj120k"  # longitud 7    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
        
    # Prueba 105
    def testCheck_passwordLengthSevenNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "1F09ir2"  # longitud 7    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result) 
        
    # Prueba 106
    def testCheck_passwordLengthSeventeenInvalidCharacters(self):
        oLogin           = login() 
        message          = "(-:cpsm09JK\?|{=]"    # longitud 17    caracteres invalidos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 107
    def testCheck_passwordLengthSeventeenNotDigits(self):
        oLogin           = login() 
        message          = "#.LpeW@+lnkzA.@yl"    # longitud 17    sin digitos
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)

    # Prueba 108
    def testCheck_passwordLengthSeventeenNotDigitsNotCapitalized(self):     
        oLogin           = login() 
        message          = "k*sdj+fwei..weh@#"    # longitud 17    sin digitos ni mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)  

    # Prueba 109
    def testCheck_passwordLengthSeventeenNotDigitsNotSpecialCharacters(self):   
        oLogin           = login() 
        message          = "MJiqJwieALniDGRou"    # longitud 17    sin digitos ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
         
    # Prueba 110
    def testCheck_passwordLengthSeventeenNotCapitalized(self): 
        oLogin           = login() 
        message          = "@#$+zj*ic71c22x.."    # longitud 17    sin mayusculas
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)      
         
    # Prueba 111
    def testCheck_passwordLengthSeventeenNotCapitalizedNotSpecialCharacters(self):    
        oLogin           = login() 
        message          = "i3u48712384uioiqm"    # longitud 17    sin mayusculas ni caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)
                 
    # Prueba 112
    def testCheck_passwordLengthSeventeenNotSpecialCharacters(self):  
        oLogin           = login() 
        message          = "JFFefn93kNJK43672"    # longitud 17    sin caracteres especiales
        encriptedMessage = oLogin.encript(message)
        result           = oLogin.check_password(encriptedMessage,message)
        self.assertFalse(result)     

    ##########################################      
    #      Pruebas para Length_password      #
    ##########################################
    
    # Caso Inicial
    
    # Prueba 113
    def testLength_passwordExists(self):
        oLogin  = login() 
        oLength = oLogin.length_password("ABC.123")
        
    # Casos Malicia
    
    # Prueba 114
    def testLength_passwordLengthZero(self):
        oLogin  = login() 
        oLength = oLogin.length_password("")
        self.assertEqual(0,oLength)
        
    # Prueba 115
    def testLength_passwordOnlySpaces(self):
        oLogin  = login() 
        oLength = oLogin.length_password("   ")
        self.assertEqual(3,oLength)
        
    # Prueba 116
    def testLength_passwordLargestRepresentableNumber(self):
        oLogin  = login() 
        oLength = oLogin.length_password((2**28)*"a")
        self.assertEqual(2**28,oLength)

    # Casos Frontera
    
    # Prueba 117
    def testLength_passwordLengthSeven(self):
        oLogin  = login() 
        oLength = oLogin.length_password("M3A0$d8") # Longitud 7   
        self.assertEqual(7,oLength)
         
    # Prueba 118
    def testLength_passwordLengthEight(self):
        oLogin  = login() 
        oLength = oLogin.length_password("pa$$w0rD") # longitud 8
        self.assertEqual(8,oLength)

    # Prueba 119
    def testLength_passwordLengthSixteen(self):
        oLogin  = login() 
        oLength = oLogin.length_password("16.9rh@Ag5wxQzp0")  # longitud 16     
        self.assertEqual(16,oLength)
        
    # Prueba 120
    def testLength_passwordLengthSeventeen(self):
        oLogin  = login() 
        oLength = oLogin.length_password("C*@d$.3Aca#a3aE+$") # longitud 17
        self.assertEqual(17,oLength)

    # Casos Normales
    
    # Prueba 121
    def testLength_passwordLengthNine(self):
        oLogin  = login() 
        oLength = oLogin.length_password("pa$$w0rD.") # longitud 9
        self.assertEqual(9,oLength)
        
    # Prueba 122
    
    def testLength_passwordLengthFifteen(self):
        oLogin  = login() 
        oLength = oLogin.length_password("16.9rh@AgwxQzp0") # longitud 15 
        self.assertEqual(15,oLength)

# #Fin de Casos Login 