#Santiago Garcia Arango, 16 Enero 2020
#IMPORTAR LIBRERIAS Y OTROS ARCHIVOS REALIZADOS POR MI
#-------------------------------------------------------------------------------------
#Hay varias maneras principales de importar librerias o archivos de python...

#FORMA 1:(obtener TODO lo de ARCHIVO)
#import ARCHIVO

#FORMA 2: ( obtener TODO lo de ARCHIVO)
#from ARCHIVO import *

#FORMA 3: (obtener solo FUNCION/CLASE del ARCHIVO)
#from ARCHIVO import FUNCION/CLASE

#La diferencia entre la forma 1 y 2 es que en la primera, al llamar a las clases...
#...o metodos de ARCHIVO, se debe hacer asi:
#>>ARCHIVO.METODO()
#mientras que en la segunda (al igual que en la tercera) asi:
#>>METODO()


#-------------------------------------------------------------------------------------
#EJEMPLO...
#Se importa la libreria sys, y se devuelve los paths en donde python...
#...busca los archivos para importar (UTIL VERLOS)

import sys

#Notar que se debe utilizar el "sys._____" para acceder a funciones/metodos
#IMPORTANTE: Tambien se busca en DIR (carpeta) actual! (correr codigo y verificar)
print("PATHS:\n")
print(sys.path)
