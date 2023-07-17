from selenium import webdriver
# Seleciona un input

from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import selenium.webdriver.support.ui as ui 
import selenium.webdriver.support.select
import time

path = 'D:/Desarrollos/chromedriver_win32/chromedriver'

op = Options()

webSite1 = 'https://performancemanager8.successfactors.com/login?company=comunicaci#/login'

#options = webdriver.ChromeOptions() 
#options.add_experimental_option('excludeSwitches', ['enable-logging']) 
#service = Service(path) 
#driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Chrome(path)

driver.get(webSite1)

time.sleep(3000)

#userFill = driver.find_element_by_id('__input1')
driver.implicitly_wait(7)
print("Prueba de selección de elemento")
input_nameFill = Select(driver.find_element("ID", '__input1'))
print("Elemento Seleccionado...")
#userFild = driver.find_element("xpath", '//div[@id="__input1"]')
#input_nameFill.send_keys('Ejemplo')
#userFild.click()

input('Esperando a que no se cierre google...')

#webSite2 = "https://conectados.com.co/inicio";
