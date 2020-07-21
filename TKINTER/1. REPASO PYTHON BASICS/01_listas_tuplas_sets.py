#Santiago Garcia Arango, 15 Enero 2020
#Se trabaja con diferentes tipos de "almacenadores" de archivos...
#... en Python (LISTAS, TUPLAS, SETS)
#-------------------------------------------------------------------------------------
#1. LISTAS:
#(pensar como vector), SI tienen orden
mi_lista = ["Santiago","Javier","Daniel","Mario"]


#-------------------------------------------------------------------------------------
#2. TUPLAS:
#(diferencia con las listas) --> NO se pueden editar, a diferencia de listas y sets
#Si tienen orden
mi_tupla = ("Santiago","Javier","Daniel","Mario")

#-------------------------------------------------------------------------------------
#3. SETS:
#Muy similar, pero NO se permiten duplicados.
# Ademas NO tienen orden
#UTIL: operaciones de union, interseccion, diferencia entre sets (como si fueran conjuntos)
mi_set = {"Santiago","Javier","Daniel","Mario"}


#Imprimimos los almacenadores (muy similar) 
print( "MOSTRAMOS ARCHIVADORES: \n" )
print("LISTA: ", mi_lista )
print( "TUPLA: ",mi_tupla )
print("SET: ", mi_set )

#Imprimimos elementos ORDENADOS en listas y tuplas...
#OJO: sets NO permite esto (NO hay orden)
print( "\nMOSTRAMOS POSICION <0> : \n" )
print( mi_lista[0] )
print( mi_tupla[0] )

#Modificar elementos (solo se puede en listas)...
#Hay muchas formas de hacerlo...
#UTIL: "LISTA.append( algo )", permite agregar elemento "algo", en posicion final
#NOTA: No solo se pueden almacenar strings/numeros, tambien...
#se puede almacenar objetos y matrices, etc
print( "\nLUEGO DE MODIFICAR LISTA: \n" )
mi_lista[0] = "Santi"
mi_lista.append( "Manuela" )
print(mi_lista)
