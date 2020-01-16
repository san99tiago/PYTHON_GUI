#Santiago Garcia Arango, 15 Enero 2020
#LAMBDA FUNCTIONS...
#-------------------------------------------------------------------------------------
#Son funciones especiales, diferentes de las tradicionales.
#Estas funciones son especialmente dedicadas a obtener inputs y devolver outputs...
#...es decir NO SE USAN PARA ACCIONES, solo para inputs-->proceso-->output
#Son muy utiles en interfaces graficas y entornos virtuales que simulen "backend"
#UTIL: NO necesitan nombre, pero suelen tenerlo
#UTIL (fuera de tema) funcion "map" para ejecutar multiples funciones a una lista,tupla o set

#-------------------------------------------------------------------------------------
#Se creara funcion "suma", en formato "Lambda"...
#FORMA TRADICIONAL:
def suma_1( x, y ):
    return( x + y)

#FORMA LAMBDA:
suma_2 = lambda x,y: x + y

#Se ejecutan ambas...
print( suma_1(1,2) )
print( suma_2(1,2) )


