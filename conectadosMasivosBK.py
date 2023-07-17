from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox as mb

import subprocess
import datetime
import time
import pandas as pd # Librería para gestionar archivos de excel

# ================== Lectura de la BD en Excel ===============
# =============================================================
df = pd.read_excel("D:/Desarrollos/WebScrapingPythonSelenium/desbloqueosUsuarios/desbloqueoUsers.xlsx")
print(df)
#df.info() # Geneara la información completa del DataFrme
#filasTotales = len(df.axes[0])
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
noEncontradosActivos = []
noEncontradosEstados = []

for j in df.index:
    
    documentoUsuario = (df.loc[j, "documento_identidad"])
    
    #Ingresar documento a la barra de busqueda y clic en buscar
    print("El número tomado es: ", documentoUsuario)
    #time.sleep(2)
    driver.get(website)
    

    #try:
        
    inputDocument = driver.find_element("xpath", '//*[@class= "form-control input-group-inset input-group-inset-after"]')
    inputDocument.send_keys(str(documentoUsuario))
    #time.sleep(2)
    buscar_button = driver.find_element("xpath",'//*[@class="btn btn-unstyled"]')
    buscar_button.click()
    
    
    
    # Subproceso de JS para analizar el contenido del DOM, para el primer filtro en la pestaña "Activos"
        
    js_script = '''
    const div = document.getElementsByClassName('text-truncate')[0].textContent;
    const div2 = div.trim();
    const regex = /0 resultados para/;
    
    if (regex.test(div2)){
        return false;
    }else{
        return true;
    }
    
    '''
    div2 = driver.execute_script(js_script)
    print(div2)
    
    # Fin del subproceso
    
    
    if div2 == False:
        print("No se encontraron usurios relacionados")
        
        """
        noEncontradosActivos.append(str(documentoUsuario))
    
        fecha = datetime.datetime.now()
        col1 = "Documento" # Nombres de los encabezados de Excel
        col2 = "Estado"
    
        df2 = pd.DataFrame({col1 : noEncontradosActivos, col2 : None}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
        df2.to_excel('D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/noActivos.xlsx', sheet_name='NoActivos', index=False)
        """
        
        # Aquí se realiza una prueba para buscar por inactivos
        #============================================================
        
        btnFiltYOrdenar = driver.find_element("xpath", '//*[@class="navbar-breakpoint-down-d-none"]')
        btnFiltYOrdenar.click()
        
        # Busqueda por el dropdown de "Inactivos"
        
        btnInactivos = driver.find_element(By.LINK_TEXT, 'Inactivo')
        btnInactivos.click()
        
        time.sleep(1)
        
        print("Ingresando al apartado de inactivos, hasta aquí va OK")
        
        # Subproceso de JS para analizar el contenido del DOM, para el segundo filtro en la pestaña "Inactivos"
        
        js_script2 = '''
        const divInactivos = document.getElementsByClassName('text-truncate')[0].textContent;
        const divInactivos2 = divInactivos.trim();
        const regex = /0 resultados para/;
        
        if (regex.test(divInactivos2)){
            return false;
        }else{
            return true;
        }
        
        '''
        divInactivos2 = driver.execute_script(js_script2)
        #print("El resultado de la búsqueda por inactivos fue: ", divInactivos2)
    
         # Fin del subproceso
         
        if divInactivos2 == True:
        
            noEncontradosActivos.append(str(documentoUsuario))
            noEncontradosEstados.append("Usuario Bloqueado")
            
            col1 = "Documento" # Nombres de los encabezados de Excel
            col2 = "Estado"
            
            df2 = pd.DataFrame({col1 : noEncontradosActivos, col2 : noEncontradosEstados}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
            df2.to_excel('D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/noActivos.xlsx', sheet_name='NoActivos', index=False)
            print(df2)
    
        if divInactivos2 == False:
            
            noEncontradosActivos.append(str(documentoUsuario))
            noEncontradosEstados.append("Usuario No creado")
            
            col1 = "Documento" # Nombres de los encabezados de Excel
            col2 = "Estado"
        
            df2 = pd.DataFrame({col1 : noEncontradosActivos, col2 : noEncontradosEstados}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
            df2.to_excel('D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/noActivos.xlsx', sheet_name='NoActivos', index=False)
        

    else:
        print("Todo normal hasta aquí ")

        # Opciones de investigación
        buscar_button2 = driver.find_element("xpath",'//*[@class="table-cell-expand-small table-cell-minw-150 table-title lfr-name-column"]')
        buscar_button2.click()
        time.sleep(3)


        # ================== Gestión de credenciales ===============
        # =============================================================
        
        
        # =========================== Cambio de credenciales a 1 =====================================
        # Esto se realiza para asegurar que la contraseña no es la misma
        # ============================================================================
        
        # Selección del apartado de contraseña
        password_button = driver.find_element(By.LINK_TEXT, 'Contraseña')
        password_button.click()
        time.sleep(1)


        # Ingresar contraseña 1
        inputDocument2 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
        inputDocument2.send_keys(str(1))


        # Ingresar contraseña 2
        inputContraseña = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
        inputContraseña.send_keys(str(1))
        print("Hasta aquí va OK la repetición")

        # Guardar cambios
        guardar_button3 = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
        #guardar_button3.click()
        print("Hace clic en guardar")
        time.sleep(1)
        
        
        
        
        # =========== Correcto restablecimiento (Num de CC) ===================
        
        

        # Selección del apartado de contraseña
        password_button2 = driver.find_element(By.LINK_TEXT, 'Contraseña')
        password_button2.click()
        time.sleep(1)


        # Ingresar contraseña 1
        inputDocument3 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password1"]')
        inputDocument3.send_keys(str(documentoUsuario)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas


        # Ingresar contraseña 2
        inputContraseña2 = driver.find_element("xpath", '//*[@id= "_com_liferay_users_admin_web_portlet_UsersAdminPortlet_password2"]')
        inputContraseña2.send_keys(str(documentoUsuario)) # ---- Recordar que recibe un parametro. Tenerlo en cuenta al momento de aplicarle los cambios con Pandas
        print("Hasta aquí va OK")

        # Guardar cambios
        guardar_button4 = driver.find_element("xpath",'//*[@class="btn  btn-primary btn-default"]')
        #guardar_button4.click()
        print("Hace clic en guardar")
        time.sleep(2)
        
        

        # =============================================================


        # ================== Retornar a la busqueda ===============
        # =============================================================
        driver.get(website)

        time.sleep(2)

    # =============================================================

    driver.get(website)
    # =============================================================

# Clase de la alerta = alert alert-dismissible alert-danger

#mb.showinfo(message="Proceso finalizado", title="Ejecución Exitosa")
#driver.quit()

input('El proceso ha finaizado con éxito!... De un enter para salir')

