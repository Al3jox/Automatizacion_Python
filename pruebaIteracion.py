import pandas as pd
import datetime

df = pd.read_excel("D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/usuarios.xlsx")
#df2 = pd.read_excel("D:/Desarrollos/WebScrapingPythonSelenium/PrubaIteracionPandas/noActivos.xlsx")
#print(df)
"""
numFilas = len(df.axes[0])
numColumnas = len(df.axes[1])

print("El número de registros es de: %i" % numFilas)
print("El número de columnas es de: %i" % numColumnas)
"""


#df.info() # Muestra las generalidades del DF
#print(df.columns) # Muestra los nombres de las columas y detalles
#print(df.info(verbose=True)) # Muestra detalladamente los campos
#print(df.shape) # Muestra las filas y columnas
#print(df.shape[0]) # Muestra solo las Filas
#print(df.shape[1]) # Muestra solo las columnas

"""
for i in range(len(df)):
    print(df.iloc[[0],:])
"""
    
    

for i in df.index:
    print(df.loc[i, "CEDULA"], str(df.loc[i, "NOMBRE_1"])) # Nota: Los nombres de los campos en la BD, NO PUEDEN TENER ESPACIOS

"""    
print(df2)

arryMotos =[]

moto1 = "Yamaha"
moto2 = "Honda"
moto3 = "BMW"

arryMotos.append(moto1)
arryMotos.append(moto2)
arryMotos.append(moto3)

fecha = datetime.datetime.now()

col1 = "Marcas" # Nombres de los encabezados de Excel
    
df2 = pd.DataFrame({col1 : arryMotos}) # pd.DataFrame({col1 : arryMotos, col2 : arreglo2})
df2.to_excel('./pruebaGuardadoMotos.xlsx', sheet_name='Motos', index=False)


try:
    
    col1 = "x"
    
    data = pd.DataFrame({col1 : arryMotos})
    data.to_excel('pruebaGuardadoMotos', sheet_name='Motos' + str(fecha.hour), index=False)
    
except:
    print("Error al guardar en el archivo")

for i in range(len(arryMotos)):
    print("El arreglo de mosots contiene: ", arryMotos[i])


#print(df2)
 """ 




