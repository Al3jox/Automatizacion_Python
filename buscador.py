from selenium import webdriver
import time

website ='https://www.mrpc.com.co'

path = 'D:/Desarrollos/chromedriver_win32/chromedriver'

# Genera la consulta

driver = webdriver.Chrome(path)
driver.get(website)

time.sleep(3)

#mas_Categ_button = driver.find_element("xpath",'//*[@id="masthead"]/div/div[3]/div[1]/div/div')
Categ_button = driver.find_element("xpath",'//*[@class="box-category"]')
Categ_button.click()

#listaRamButton = driver.find_element(By.)
#listaRamButton.click()

input('Esperando a que no se cierre google...')