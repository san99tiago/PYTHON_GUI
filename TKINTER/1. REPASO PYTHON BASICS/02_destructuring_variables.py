#Santiago Garcia Arango, 15 Enero 2020
#VECTORES Y TUPLAS COMBINADAS + LEER TUPLA
#-------------------------------------------------------------------------------------
# #Manejo de tuplas y acceder a informacion

#Se crea un vector de personas, cuyos elementos son tuplas...
personas = [ ("Brayan",40,"Desempleado"),("Daniela",21,"Estudiante"),("Juanita",30,"Ingeniera") ]

#-------------------------------------------------------------------------------------
#FORMA 1: Forma poco aconsejable de mostrar info:
print("FORMA 1: \n")
print(personas)

#-------------------------------------------------------------------------------------
#FORMA 2: mucho mejor y mas organizada de mostrar info:
print("\nFORMA 2: \n")
#Se crean "desestructuras" para descomponer tuplas
for nombre,edad,profesion in personas:
    #OJO: mirar "f" como asignador de las variables...
    print( f"NOMBRE: {nombre} , EDAD: {edad}, PROFESION: {profesion}" )

#-------------------------------------------------------------------------------------
#DATO CURIOSO: Si NO nos interesara por ejemplo, la edad...
#FORMA 3: organizado, SIN mostrar edad:
#Se debe agregar el "_" para decir que esa variable es OBSOLETA/IGNORADA
print("\nFORMA 3: \n")
for nombre, _, profesion in personas:
    print( f"NOMBRE: {nombre} , PROFESION: {profesion}" )
