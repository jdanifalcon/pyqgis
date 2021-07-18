#importamos las librerias de pyQGIS
from PyQt5.QtCore import QVariant
from qgis.core import *

#cargamos la capa de trabajo
shp = r"C:\prueba\clip_Lagunas.shp"
layer = QgsVectorLayer(shp,'clipLagunas','ogr')

#Expresión para calcular area
expression1 = QgsExpression('$area')

#Creamos el contexto y cargamos la capa
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

#Activamos la edición de la capa
with edit(layer):
    #Recorremos cada entidad en la Capa
    for f in layer.getFeatures():
        #aplicamos la expresión a cada entidad
        context.setFeature(f)
        f['Area_m2'] = expression1.evaluate(context)
        #Guardamos la edición realizada
        layer.updateFeature(f)

print("Area Calcualda")