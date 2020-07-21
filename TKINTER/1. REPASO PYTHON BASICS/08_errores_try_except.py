#Santiago Garcia Arango, 16 Enero 2020
#MANEJO DE ERRORES ---> TRY/EXCEPT
#-------------------------------------------------------------------------------------

#Los errores son formas correctas y elegantes de indicar que ha sucedido...
#... un evento NO deseado y que puede ser comun que pase.

#El objetivo es lograr sobrepasar los errores, dandonos cuenta de estos, y a la vez...
#... permitir que el codigo continue y haga algo con respecto al error, sin necesariamente...
#... tener que separar esencia de error, con sentido error del programa
#Lograremos esto a traves de dos etapas:

#PRIMERA ETAPA:
#En FUNCION/METODO, incluir posible error que suceda...

#>>FUNCION/METODO( PARAMETROS):
#>>    if RAZON_ERROR)_CONOCIDA:
#>>        raise ERROR("INDICADOR ERROR CONOCIDO")
#>>    return ( RESULTADO )

#SEGUNDA ETAPA:
#En codigo ya funcional, cuando se llame la funcion, agrega try-except...
#...de tal forma que se logre obtener el error y sobrepasarlo...

#>>try:
#>>    FUNCION/METODO_CON_POSIBLE_ERROR()
#>>except ERORR_CONOCIDO:        
#>>    print("EL ERROR FUE ESTE")
#>>else:
#>>    CODIGO QUE CORRE SI NO HAY ERRORES
#>>finally:
#>>    ESTO SIEMPRE SIEMPRE CORRE, CON O SIN ERROR

#NOTA: en "except", se pueden poner varios tipos de errores si se necesita

#Se pueden crear "Errors" propios, y la logica es la misma (ambas etapas)
#SI SE NECESITA, BUSCAR COMO CREAR ERRORES PROPIOS


#-------------------------------------------------------------------------------------
#EJEMPLO:
#Manejo de error division por cero en programa sencillo
#Correr programa y ver error corregido en terminal 

#Se crea funcion que incluya posibilidad de division por cero
def dividir(x,y):
    #En caso de tener denominador nulo, se hace "raise" error...
    if y == 0:
        raise ZeroDivisionError( "El divisor NO puede ser cero." )
   
    #En caso de que NO haya denominador nulo, se devuelve resultado
    return( x/y )

#Se ejecuta codigo, con "TRY" y "EXCEPT"
a = 10
b = 0
try:
    print( dividir(a,b) )
except ZeroDivisionError:
    print( "RECORDAR QUE DENOMINADOR NO PUEDE SER NULO!" )
finally:
    print("GRACIAS POR DIVIDIR CON SANTI")

