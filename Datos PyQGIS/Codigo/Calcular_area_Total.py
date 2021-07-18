#importamos las librerias de pyQGIS
from qgis.core import *

#cargamos la capa de trabajo
shp = r"C:\prueba\clip_Lagunas.shp"
layer = QgsVectorLayer(shp,'clipLagunas','ogr')

#Creamos una variable para el área total
total_area = 0

for laguna in layer.getFeatures():
    #Almaceno el area de cada laguna
    area = laguna["area_m2"]
    #suma el area de cada laguna
    total_area += area

#mostramos el resultado
print ("Area Total: "+ str(total_area)+' m2')