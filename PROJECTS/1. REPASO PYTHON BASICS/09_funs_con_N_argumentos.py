#Santiago Garcia Arango, 16 Enero 2020
#FUNCIONES/METODOS CON CUALQUIER CANTIDAD DE ARGUMENTOS/PARAMETROS
#-------------------------------------------------------------------------------------

#Esta estrategia nos permite crear funciones con cualquier cantidad de argumentos...
#... son fundamentales a la hora de permitir emplear ciertos parametros segun caso.
#... y NO tienen error por dar menos argumentos que el total.


#*ARGUMENTS:
#Se denotan en parametros como (*args)
#Son cualquier tipo de variable que luego ingresa como tupla en funcion/metodo...
#Permiten ingresar N cantidad de parametros a una funcion, sin importar cuantos sean.

#**KEYWORD ARGUMENTS:
#Se denotan en parametros como (**kwargs)
#Son cualquier tipo de datos ingresados en formato diccionario, y se almacenan igual...
#...en metodo o funcion, permitiendo identificacion total al recibirlo.
#Se obtiene un diccionario con la "key" siendo el nombre del parametro...
#...y la pareja el parametro que el usuario quiere ingresar


#OJO: importante tener en cuenta que al agregar almenos 1 parametro normal, o un kwarg...
#...se hace obligatorio indicar en parametros de funcion, el nombre de este parametro asi:
# FUNCION( PAR_1 = algo, PAR_2 = algo, PAR_3 = algo ), de lo contrario, python no sabe cual es cual

#-------------------------------------------------------------------------------------
#EJEMPLO 1:
#Crear funcion que multiplique N cantidad de numeros, recibidos como parametros
print("\n\n" + "*"*15 + " EJEMPLO 1 (ARGS): " + "*"*15)

def productoria(*args):
    print("LA PRODUCTORIA DE")
    print(args)
    print("ES UN TOTAL DE :")
    total = 1
    for arg in range( len(args) ):
        total = total * args[arg]
    print(total)

productoria( 1,2,3,4,5,6 )


#-------------------------------------------------------------------------------------
#EJEMPLO 2:
#Crear funcion que devuelva la info como diccionario, segun los parametros entregados...
#...independiente del kw y valor empleado
print("\n\n" + "*"*15 + " EJEMPLO 2 (KWARGS): " + "*"*15)
def dame_mi_info(**kwargs):
    #Mostramos como llega la info...
    print("ASI LLEGA INFO:")
    print(kwargs)
    #Ahora se mostrara la info bonita...
    print("\nASI LA PROCESAMOS:")
    #OJO: se crea kw y valor para cada item de kwargs...
    #...se recorre kwargs como kwargs.items(), porque es diccionario
    for kw , valor in kwargs.items():
        print("{} : {}".format(kw,valor))

#Se crea funcion con muchos valores especificados, sea los que sea
dame_mi_info(nombre = "Santiago",apellido = "Garcia", edad = 20, sexo = "Masculino")


#-------------------------------------------------------------------------------------
#EJEMPLO 3:
#Ejemplo que involucre valores asociados a los "args" y diccionarios asociados a los "kwargs"
print("\n\n" + "*"*15 + " EJEMPLO 3 (ARGS + KWARGS): " + "*"*15)

#Se procesa info que muestra el formato en que almacena info de args y kwargs
def procesar_args_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

#Se crea funcion con args y kwargs locos, sin sentido, pero que explica funcionamiento
procesar_args_kwargs(1,2,5,6,3, idioma = "Espannol", carrera = "Mecatronica", sexo = "Masculino", otro = 25)

