from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time                           import sleep

browser = webdriver.Firefox()

browser.get('http://0.0.0.0:5000')
assert 'scrum' in browser.title

user = browser.find_element_by_id('fLogin_usuario')
user.send_keys('reiverdugo')
password = browser.find_element_by_id('fLogin_clave')
password.send_keys('ve@7IVlv' + Keys.RETURN)
from time                           import sleep
assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'

sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Historias')])").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'+Tarea')])").click()
sleep(2)
descripcion = browser.find_element_by_id('fTarea_descripcion')
descripcion.send_keys('work ft. drake')

# browser.quit()
