from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox as mb

import datetime
import time
import pandas as pd # Librería para gestionar archivos de excel

# ================== Lectura de la BD en Excel ===============
# =============================================================
df = pd.read_excel("D:/Desarrollos/WebScrapingPythonSelenium/desbloqueosUsuarios/desbloqueoUsers.xlsx")
print(df)
#df.info() # Geneara la información completa del DataFrme
filasTotales = len(df.axes[0])
#columnasTotales = len(df.axes[1])
#print("Filas totales: %i" % filasTotales)
#print("Columnas totales: %i" % columnasTotales)

# =============================================================


# ================== Ingreso a la plataforma ===============
# =============================================================

website ='https://conectados.com.co/group/control_panel/manage?p_p_id=com_liferay_users_admin_web_portlet_UsersAdminPortlet&p_p_lifecycle=0&p_p_state=maximized&p_v_l_s_g_id=336077'

path = 'D:/Desarrollos/chromedriver_win32/chromedriver'

# Genera la consulta

driver = webdriver.Chrome(path)
driver.get(website)

time.sleep(3)

Categ_button = driver.find_element("xpath",'//*[@class="sign-in-uclaro mr-4"]')
Categ_button.click()

# Inserción  de datos en los inputs del login
#User Name
inputElement = driver.find_element("xpath", '//*[@id= "_co_com_claro_conectados_login_LoginPortlet_INSTANCE_true_userName"]')
inputElement.send_keys('1015465005')

#Password
inputElement = driver.find_element("xpath", '//*[@id= "_co_com_claro_conectados_login_LoginPortlet_INSTANCE_true_password"]')
inputElement.send_keys('Con31415*')

#Capcha wait
time.sleep(10)

#Botón de ingresar
ingresar_button = driver.find_element("xpath",'//*[@class="ingresarBoton"]')
ingresar_button.click()
time.sleep(2)


for j in df.index:
    
    documentoUsuario = (df.loc[j, "documento_identidad"])
    
    #Ingresar documento a la barra de busqueda y clic en buscar
    print("El número tomado es: ", documentoUsuario)
    #time.sleep(2)
    driver.get(website)
    #noEncontradosActivos = []

    #try:
        
    inputDocument = driver.find_element("xpath", '//*[@class= "form-control input-group-inset input-group-inset-after"]')
    inputDocument.send_keys(str(documentoUsuario))
    #time.sleep(2)
    buscar_button = driver.find_element("xpath",'//*[@class="btn btn-unstyled"]')
    buscar_button.click()
    
    #except ValueError as err:
    """print("Error:", err)
    noEncontradosActivos.append(str(documentoUsuario))
    
    fecha = datetime.datetime.now()
    col1 = "Documento" # Nombres de los encabezados de Excel
    
    df2 = pd.DataFrame({col1 : noEncontradosActivos}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
    df2.to_excel('D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/noActivos.xlsx', sheet_name='NoActivos', index=False)
    
    print("El usuario no se encuentra en la pestaña de Activos")
    """
    # =============================================================


    # Opciones de investigación
    buscar_button = driver.find_element("xpath",'//*[@class="table-cell-expand-small table-cell-minw-150 table-title lfr-name-column"]')
    buscar_button.click()
    time.sleep(3)


    # ================== Gestión de credenciales ===============
    # =============================================================
    
    
    # =========================== Repetición =====================================
    # ============================================================================
    
       # Selección del apartado de contraseña
    password_button = driver.find_element(By.LINK_TEXT, 'Contraseña')
    password_button.click()
    time.sleep(1)


    # Ingresar contraseña 1
    inputDocument = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
    inputDocument.send_keys(str(1)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas


    # Ingresar contraseña 2
    inputContraseña = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
    inputContraseña.send_keys(str(1)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas
    print("Hasta aquí va OK la repetición")

    # Guardar cambios
    guardar_button = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
    guardar_button.click()
    time.sleep(1)
    
    
    
    
    # =========== Correcto restablecimiento (Num de CC) ===================
    
    

    # Selección del apartado de contraseña
    password_button = driver.find_element(By.LINK_TEXT, 'Contraseña')
    password_button.click()
    time.sleep(1)


    # Ingresar contraseña 1
    inputDocument = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
    inputDocument.send_keys(str(documentoUsuario)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas


    # Ingresar contraseña 2
    inputContraseña = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
    inputContraseña.send_keys(str(documentoUsuario)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas
    print("Hasta aquí va OK")

    # Guardar cambios
    guardar_button = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
    guardar_button.click()
    #print("Hace clic en guardar")
    time.sleep(1)
    
    

    # =============================================================


    # ================== Retornar a la busqueda ===============
    # =============================================================
    driver.get(website)

    time.sleep(2)

# =============================================================


# =============================================================


# Clase de la alerta = alert alert-dismissible alert-danger
mb.showinfo(message="Proceso finalizado", title="Ejecución Exitosa")
input('Esperando a que no se cierre google...')

