import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def wait(self):
        time.sleep(4) 

    def testLogin(self):

        self.wait()
        driver = self.driver
        driver.get("http://0.0.0.0:5000/#/VLogin")
        self.wait()
        user = driver.find_element_by_name("usuario")
        user.send_keys("T3l3p1zz4@")

        password = driver.find_element_by_name("clave")
        password.send_keys("T3l3p1zz4@")
        self.wait() 
        password.submit()

        #Vamos a prelaciones
        self.wait()
        self.wait()
        driver.get("http://0.0.0.0:5000/#/VProducto/1")
        self.wait()
        driver.get("http://0.0.0.0:5000/#/VHistorias/1")
        self.wait()
        driver.get("http://0.0.0.0:5000/#/VPrelaciones/1")


    def tearDown(self):
        self.wait()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()