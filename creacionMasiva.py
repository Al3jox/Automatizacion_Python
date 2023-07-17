from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox as mb
from dateutil import parser
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import datetime
import time
import pandas as pd # Librería para gestionar archivos de excel

# Importación del archivo de funciones
import functionsCrecionMasivos as fn

# ================== Lectura de la BD en Excel ===============
# =============================================================
df = pd.read_excel("D:/Desarrollos/WebScrapingPythonSelenium/BD_New_Users/New_Users.xlsx")
print(df)

# Recorrido del DF
fn.recorrerDF(df)

# Ingreso a la plataforma
website ='https://conectados.com.co/group/control_panel/manage?p_p_id=com_liferay_users_admin_web_portlet_UsersAdminPortlet&p_p_lifecycle=0&p_p_state=maximized&p_v_l_s_g_id=336077'

# Ruta del driver
path = 'D:/Desarrollos/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

usersNotCreated = []
usersNotCreatedStatus = []

time.sleep(3)

# Click en el btn de login 
Categ_button = driver.find_element("xpath",'//*[@class="sign-in-uclaro mr-4"]')
Categ_button.click()

# Inserción  de datos en los inputs del login
#User Name
inputElementUser = driver.find_element("xpath", '//*[@id= "_co_com_claro_conectados_login_LoginPortlet_INSTANCE_true_userName"]')
inputElementUser.send_keys(fn.userID())

#Password
inputElementPass = driver.find_element("xpath", '//*[@id= "_co_com_claro_conectados_login_LoginPortlet_INSTANCE_true_password"]')
inputElementPass.send_keys(fn.userPass())

#Capcha wait
time.sleep(10)

ingresar_button = driver.find_element("xpath",'//*[@class="ingresarBoton"]')
ingresar_button.click()

time.sleep(2)

# Link de creación de usuarios
website2 = "https://conectados.com.co/group/control_panel/manage?p_p_id=com_liferay_users_admin_web_portlet_UsersAdminPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_users_admin_web_portlet_UsersAdminPortlet_mvcRenderCommandName=%2Fusers_admin%2Fedit_user"


for i in df.index:
    
    dataUserId = (df.loc[i, "CC"])
    dataUserEmail = (df.loc[i, "correo"])
    dataUserPosition = (df.loc[i, "cargo"])
    dataUserBirthday = (df.loc[i, "fechaNacimiento"])
    dataUserName = (df.loc[i, "nombres"])
    dataUserLastName = (df.loc[i, "apellidos"])
    dataUserRegion = (df.loc[i, "regional"])
    dataUserChannel = (df.loc[i, "canal"])
    dataUserCompany = (df.loc[i, "empresa"])
    
    
    print(dataUserPosition)
    
    time.sleep(2)
    
    print('Hasta aquí todo va OK')
    
    driver.get(website2)

    # Rellenar campos
    userIdField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_screenName"]')
    userIdField.send_keys(str(dataUserId))

    userEmailFiel = driver.find_element("xpath", '//*[@id = "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_emailAddress" ]')
    userEmailFiel.send_keys(str(dataUserEmail))
    
    userPositionField = driver.find_element("xpath", '//*[@id = "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_jobTitle" ]')
    userPositionField.send_keys(str(dataUserPosition))
    
    userBirthField = driver.find_element("xpath", '//*[@id = "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_birthday" ]')
    # Conversión de formato según la plataforma
    date_object = parser.parse(str(dataUserBirthday))
    date_formatted = date_object.strftime("%d/%m/%Y")
    userBirthField.clear()
    userBirthField.send_keys(str(date_formatted))
    
    userNameField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_firstName"]')
    userNameField.send_keys(str(dataUserName))
    
    userLastNameField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_lastName"]')
    userLastNameField.send_keys(str(dataUserLastName))
    
    userRegionField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_scch___Region"]')
    userRegionField.send_keys(str(dataUserRegion))
    
    userChannelField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_qixe___canal"]')
    userChannelField.send_keys(str(dataUserChannel))
    
    userCompanyField = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_uyuj___empresa"]')
    userCompanyField.send_keys(str(dataUserCompany))
    
    # Scroll totalmente a la parte inferior de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(1)
    
    print("Id: ", dataUserId)
    print("Email: ", dataUserEmail)
    print("Cargo: ", dataUserPosition)
    print("Fecha: ", date_formatted)
    print("Nombres: ", dataUserName)
    print("Apellidos: ", dataUserLastName)
    print("Región: ", dataUserRegion)
    print("Canal: ", dataUserChannel)
    print("Empresa: ", dataUserCompany)

    
    # Click en guardar
    btnSave = driver.find_element(By.XPATH, "//span[contains(text(), 'Guardar')]")
    btnSave.click()
    
    time.sleep(2)
    
    # Validación de existencia de usuario con subprocesos de JS
    
    # tiempo_limite = 10
    # alerta_visible = WebDriverWait(driver, tiempo_limite).until(
    # EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-dismissible.alert-danger"))
    # )
    
    # if alerta_visible:
    #     print("Usuario ya creado. Se registrará en el archivo de resumen de usuarios a escalar")
        
    #     usersNotCreated.append(str(dataUserId))
    #     usersNotCreatedStatus.append("Usuario ya creado")
        
    #     col1 = "Documento" # Nombres de los encabezados de Excel
    #     col2 = "Estado"
        
    #     df2 = pd.DataFrame({col1 : usersNotCreated, col2 : usersNotCreatedStatus}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
    #     df2.to_excel('D:/Desarrollos/WebScrapingPythonSelenium/BD_New_Users/usuariosYaCreados/usuariosYaCreados.xlsx', sheet_name='YaCreados', index=False)
    #     print(df2)
        
    # else:
    #     print("Se inicia el proceso de asignación de contraseña.")
        
    #     # Selección del apartado de contraseña
    #     password_button = driver.find_element(By.LINK_TEXT, 'Contraseña')
    #     password_button.click()
    #     time.sleep(1)

    #      # Ingresar contraseña 1
    #     inputDocument3 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
    #     inputDocument3.send_keys(str(dataUserId)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas


    #     # Ingresar contraseña 2
    #     inputContraseña2 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
    #     inputContraseña2.send_keys(str(dataUserId)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas

    #     # Guardar cambios
    #     guardar_button4 = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
    #     guardar_button4.click()
    #     #print("Hace clic en guardar")
        
    #  ============================================== > Contraseña forzada
    
    print("Se inicia el proceso de asignación de contraseña.")
        
    # Selección del apartado de contraseña
    password_button = driver.find_element(By.LINK_TEXT, 'Contraseña')
    password_button.click()
    time.sleep(1)

        # Ingresar contraseña 1
    inputDocument3 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
    inputDocument3.send_keys(str(dataUserId)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas


    # Ingresar contraseña 2
    inputContraseña2 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
    inputContraseña2.send_keys(str(dataUserId)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas

    # Guardar cambios
    guardar_button4 = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
    guardar_button4.click()
    #print("Hace clic en guardar")
    
    # =============================================== > Fin contraseña
        
    time.sleep(4)
    
    # print("Se hizo click en guardar")
    
    print(" ==== > Usuario N°: " , i+1, " - ", dataUserId, " < ====")
    
    
print("** ================================ **")
print(" >  Proceso finalizado con éxito!!.  < ")
print("** ================================ **")
    