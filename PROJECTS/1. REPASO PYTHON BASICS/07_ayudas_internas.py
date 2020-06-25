#Santiago Garcia Arango, 16 Enero 2020
#AYUDAS INTERNAS CODIGO (TYPE: HINTNG)
#-------------------------------------------------------------------------------------
#La idea basica de este tema es ayudar al programador a rectificar que los parametros que...
#...se esten indicando, coincidan con la info que deberian ser, a traves de editor de texto...
#...en este caso VSCODE nos ayuda a eso.
#FORMA DE LOGRARLO:
#Al definir funcion/metodo, agregar tipo de variable, es decir:
#>>def NOMBRE( VARIABLE_1 : TIPO_VARIABLE_1, VARIABLE_2: TIPO_VARIABLE_2 ):


#-------------------------------------------------------------------------------------
#EJEMPLO:

#Se importa esto, para mostrar ayuda de info de las listas...
from typing import List
#Se crean clases normales, pero en parametros, se agregan las ayudas
class Libro:
    def __init__(self, nombre:str, paginas:int,editorial:str,autor:str):
        pass
class Repisa_Libros:
    def __init__(self,marca_repisa:str,color_repisa:str, vector_libros:List[Libro]):
        pass



#Como ver ayuda???
#En este editor, al escribir el codigo y crear los objetos, aparece el tipo de variable del parametro
L1 = Libro( "Las intermitencias de la muerte", 350,"norma","Saramago" )
L2 = Libro( "La Donante",300,"No definida","Jorge Garcia" )

vector_libros = [L1,L2]

R1 = Repisa_Libros( "Home Center","Negra", vector_libros )
