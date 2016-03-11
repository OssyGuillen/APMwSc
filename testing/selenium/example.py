from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://0.0.0.0:5000')
assert 'scrum' in browser.title

user = browser.find_element_by_id('fLogin_usuario')  # Find the search box
user.send_keys('gaga')
password = browser.find_element_by_id('fLogin_clave')  # Find the search box
password.send_keys('ve@7IVlv' + Keys.RETURN)

assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'


# browser.quit()