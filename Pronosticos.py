#!/usr/bin/env python
# coding: utf-8

# In[56]:


#Proyecto - Análisis de pronósticos de ventas
#Diana Barboza, Juan Caro e Ivan Salazar
#Extracción de datos de ventas desde un archivo .csv
import pandas as pd
import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt
#Mostrar solo dos decimales
def formato(dato):
    return "{0:.2f}".format(dato)
#Quitar puntos al User name random.randint(20,100)
def ClearDots(text):
    forbidden = {"?", "¿", "¡", "!", " ", ",", ".", ";", ":"}
    return "".join(c for c in text.lower() if c not in forbidden)
#Pone un numero aleatorio en los datos faltantes
def CleanData(cell):
    cell=ClearDots(cell)
    #Crear lista con el randint y concatenar los valores generados
    if(cell=="n.a." or cell=="-1" or cell=="not available" or cell=="NaN"):
        return random.randint(40,58)
    return cell
Ventas=pd.read_csv('Ventas.csv',index_col=0,usecols=['Ventas','Periodo'],sep=";",encoding='UTF-8',converters={'Ventas':CleanData})
print("ANÁLISIS DE MÉTODOS DE PRONÓSTICOS DE VENTAS")
print("Aplicado a Industrias Metalmecánicas San Judas Ltda.\n")
print("DATOS CARGADOS DESDE EL ARCHIVO\n")
print(Ventas)
y=np.array(Ventas['Ventas'], dtype=int)
ListaAux=[]
for i in range (0,len(y)):
    ListaAux.append(i+1)
x=np.array(ListaAux)

#Visualizar los datos gráficamente

#PRONOSTICOS
print("\nRESULTADOS DE LAS REGRESIONES")
#Regresión Lineal
Reg1=np.polyfit(x,y,1)
print("\n Regresión lineal")
print ("Y = ",formato(Reg1[1])," + ",formato(Reg1[0]),"x")

#Regresión Polinomial de grado 2
Reg2=np.polyfit(x,y,2)
print("\n Regresión polinomial de segundo grado")
print ("Y = ",formato(Reg2[2])," + ",formato(Reg2[1]),"x"," + ",formato(Reg2[0]),"x^2")

#Regresión Polinomial de grado 3
Reg3=np.polyfit(x,y,3)
print("\n Regresión polinomial de tercer grado")
print ("Y = ",formato(Reg3[3])," + ",formato(Reg3[2]),"x"," + ",formato(Reg3[1]),"x^2"," + ",formato(Reg3[0]),"x^3")

print("\nRESULTADOS DE LOS PRONÓSTICOS\n")
y1=[]
y2=[]
y3=[]
for i in range (len(x)):
    y1.append(Reg1[1]+Reg1[0]*x[i])
    y2.append(Reg2[2]+Reg2[1]*x[i]+Reg2[0]*x[i]*x[i])
    y3.append(Reg3[3]+Reg3[2]*x[i]+Reg3[1]*x[i]*x[i]+Reg3[0]*x[i]*x[i]*x[i])

Ventas['Reg. LINEAL']= pd.DataFrame(y1)                 
Ventas['Reg. Pol. GRADO 2']= pd.DataFrame(y2)   
Ventas['Reg. Pol. GRADO 3']=  pd.DataFrame(y3)
print (Ventas)

#ERRORES
print ("\nANÁLISIS DE LOS PRONÓSTICOS - (R^2)\n")
#Calculo de errores
def calculo_R2(yreal,ypron):
    sumayreal=0
    for i in range (len(ypron)):
        sumayreal+=yreal[i]
    yrpromedio=sumayreal/len(yreal)
    res=0
    res2=0
    for i in range (len(ypron)):
        res+=(ypron[i]-yrpromedio)**2
        res2+=(yreal[i]-yrpromedio)**2
    return res/res2
#Comparación de errores
metodos=["Reg. Lineal","Reg. Pol. grado 2","Reg. Pol. grado 3"]
r2=[calculo_R2(y,y1),calculo_R2(y,y2),calculo_R2(y,y3)]
for i in range (len(r2)):
    print ("R^2 para el método ["+str(metodos[i])+"] = "+formato(r2[i]))
def posmayor (array):
    aux=0
    for i in range (len(array)):
        if(array[i]==max(array)):
            aux=i
            break
    return aux
#CONCLUSIONES
#Selección del método de prónostico
print("\nRESULTADO FINAL\n")
print("Debe seleccionarse el método ["+str(metodos[posmayor(r2)])+"] para los pronósticos de ventas porque es el que posee el mayor R^2.")


# In[ ]:





# In[ ]:




