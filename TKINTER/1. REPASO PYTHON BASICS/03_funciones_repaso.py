#Santiago Garcia Arango, 15 Enero 2020
#BASICO DE FUNCIONES EN PYTHON, DEFINIDAS POR NOSOTROS...
#-------------------------------------------------------------------------------------
#Recordemos que estas funciones son creadas por nosotros, con el nombre...
#... que queramos y pueden tener parametros o no.

#Esquema general de funciones:
#>>def NOMBRE_FUNCION( PARAMETRO/S ):
#>>    HACER ALGO
#OJO: solo se ejecuta cuando se llama, y NO se crean variables globales...
#...es decir, variables que SOLAMENTE existen en la funcion, no en codigo general.
#Se recomienda revisar "VARIABLES GLOBALES".
#OJO: Primero definir funciones y luego usarlas (NO al reves)
#UTIL: si se crea nombre funcion, pero NO se crea codigo, se puede ignorar con "pass"
#Se pueden pasar "default parameters", buscar en caso de necesitarlo
#UTIL (fuera de tema) funcion "map" para ejecutar multiples funciones a una lista,tupla o set


#-------------------------------------------------------------------------------------
#CREACION DE FUNCION SIN PARAMETROS
#Se hara funcion que devuelva la fecha completa, que NO requiera parametros...
#Se trae libreria intera para manejo de dia:
import datetime
#Se crea funcion llamada "DAME_LA_FECHA"
def DAME_LA_FECHA():
    #Se obtiene info del dia, con ayuda de la libreria datetime
    dia = datetime.date.today()
    print("HOY ES: ", dia)

#OJO: La funcion ya fue definida, PERO SE DEBE LLAMAR (asi:)
DAME_LA_FECHA()

#-------------------------------------------------------------------------------------
#CREACION DE FUNCION CON PARAMETROS
#Se crea funcion que a traves de inputs te saluda con la fecha...
def DAME_LA_FECHA_CON_NOMBRE( nombre ):
    #Se obtiene info del dia, con ayuda de la libreria datetime
    dia = datetime.date.today()
    print("HOY ES: ", dia,". Feliz dia, ", nombre )

#OJO: La funcion ya fue definida, PERO SE DEBE LLAMAR (asi:)
#Se obtiene el nombre del usuario...
nombre = str( input("INGRESE SU NOMBRE:  ") )
#Se llama funcion, teniendo en cuenta el parametro nombre, ya ingresado
DAME_LA_FECHA_CON_NOMBRE( nombre )

#NOTA: tambien se pueden devolver datos, vectores, etc...
#Aplicando en la funcion: "return( LO_QUE_QUIERO_DEVOLVER )"