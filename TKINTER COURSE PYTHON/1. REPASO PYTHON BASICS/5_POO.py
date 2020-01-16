#Santiago Garcia Arango,15 Enero 2020
#PROGRAMACION ORIENTADA A OBJETOS
#-------------------------------------------------------------------------------------
#La programacion orientada a objetos es una rama de programacion muy util y empleada en python
#Su esencia es trabajar con "OBJETOS", que "HACEN" y que "SON/TIENEN", permitiendo estructurar...
#... la logica de los codigos en estos objetos de forma encapsulada o sintetizada.
#Es como crear un codigo que se componga de muchos objetos, con sus ATRIBUTOS(lo que son) y sus METODOS(lo que hacer)...
#...luego, jugar con estas cualidades y facilitar codigo de muchas formas, como:
#VENTAJAS POO
#0. Similar al pensamiento humano planteado por Kant del "Mundo de los Objetos"
#1. Mas facil de entender, crear y manejar en caso de cambios
#2. Mas organizado, con posibilidad de trabajar en multiples desarrollos en un codigo
#3. Permite reutilizar mucho codigo, dando diferencias si es necesario, con menor lineas
#4. Excelente para establecer relaciones jerarquicas
#5. Muy utilizado en apps, web, backend, GUIs, etc
#6. Muy facil de utilizar, una vez entendido
#7. Python es excelente en OOP (Objecto Oriented Programming)
#DESVENTAJAS POO
#0. En grandes bases de datos, puede llegar a ser ineficiente
#1. Puede ser una curva de aprendizaje mayor a la programacion tradicional
#2. Puede generar procesamientos lentos en cierto tipos de problemas o enfoques de programacion

#CLASES: Son lo equivalente a los "objetos" que pensamos... (HACEN - SON/TIENEN)
#Las clases se crean para poder estructurar la logica de los objetos, sin embargo...
#... los objetos NO se crean al crear las clases, sino que se deben "llamar", como las funciones

#Estructura clases:
#>>class NOMBRE_CLASE:
#>>    def __init__(self, OTROS_PARAMETROS):
#>>        LO QUE SE EJECUTA AL CREARSE EL OBJETO
#>>    def METODOS(self, LO_QUE_NECESARIO):
#>>        LO QUE SE EJECUTA AL LLAMAR AL METODO (FUNCIONES DENTRO DE CLASES)

#OJO: "self" es la correcta forma de indicarle a Python que se trata de la info o cosas del objeto
#Siempre que se guarde o cree cosas del objeto, se emplea self...

#Llamar la clase (crear el objeto):
#>>NOMBRE_OBJETO = NOMBRE_CLASE( OTROS_PARAMETROS )

#Ejecutar metodos de la clase: 
#>>NOMBRE_OBJETO.METODO( PARAMETROS_METODO )

#Acceder a info del objeto: (NOTA: mirar que NO tiene parentesis, a diferencia de los metodos que SI)
#>>NOMBRE_OBJETO.INFO_DESEADA


#UTIL: Metodos Magicos --> (__str__) y (__rpr__) para devolver info de objeto de forma especial
#Se usan estos metodos magicos para facilitar el trabajo a la hora de acceder a info de objeto

#-------------------------------------------------------------------------------------
#EJEMPLO:
#CREAR ORGANIZADOR DE PROYECTOS CON SU INFO, Y DATOS DE SU PERSONAL DE TRABAJO.


#Se crea Clase enfocada a contener info de varios proyectos, y luego se devuelve organizada
#Se crea Classe enfocada a tener info de personas involucradas en los proyectos

#Primero creamos la clase Proyecto con su respectivo __init__ que permite inicializarla
class Proyecto:
    #El inicializador o contructor recibe los parametros iniciales y luego crea variables...
    #... a nivel de guardarlas dentro del objeto. notar que pueden ser tambien listas, tuplas, int, str, etc
    def __init__(self,nombre_proyecto,personas_involucradas,fecha_creacion,presupuesto_proyecto):
        #Se guardan los parametros de interes (siempre son "self._______")
        self.nombre_proyecto = nombre_proyecto
        self.personas_involucradas = personas_involucradas
        self.fecha_creacion = fecha_creacion
        self.presupuesto_proyecto = presupuesto_proyecto
    
    #Se crea metodo para devolver info "bonita" de los proyectos
    #Notar que NO es necesario agregar parametros, pues toda la info ya esta inmortalizada en objeto
    def devolver_info(self):
        print("-----------------------------------------------------")
        print( "\nINFO PROYECTO:\n")
        print("NOMBRE PROYECTO:\n " + self.nombre_proyecto)
        print("\nFECHA CREACION PROYECTO:\n "+ self.fecha_creacion)
        print("\nPRESUPUESTO:\n " + str(self.presupuesto_proyecto) )
        print("\nPERSONAS INVOLUCRADAS:\n")
        for i in range( len(self.personas_involucradas) ):
            #Se recorre vector personas involucradas, accediendo a cada objeto(persona) y devolviendo su info...
            #... a traves de su metodo creado en esta clase (facilitando trabajo)
            self.personas_involucradas[i].devolver_info_persona()
        print("-----------------------------------------------------")


#Como los proyectos involucran personas, se debe tener todas las personas organizadas, por su info...
#...para esto se crea clase de Persona, con el objetivo de almacenar todos los datos de las personas,...
#... en estos objetos que luego se ingresaran correctamente en cada proyecto.
#...es decir, la jerarquia de las relaciones es:
# Proyectos --> (nombre, fecha,presupuesto, LISTA_PERSONAS)
# Persona --> (nombre, edad, profesion, ID)
#Lo que implica que cada proyecto a su vez, tiene interna la info de las personas en un vector de objetos (de Personas)
class Persona:
    #Se inicializa cada persona, al ser creada, almacenando su info en objeto 
    def __init__(self,nombre_persona, edad, profesion, ID):
        #Se pasa toda la info de parametros, a inmortalizar en objeto
        self.nombre_persona = nombre_persona
        self.edad = edad
        self.profesion = profesion
        self.ID = ID
    
    #Se crea Metodo, que permite devolver info de cada persona de forma organizada...
    #...esto sera importante para clase "Proyecto", al devolver info en esta del proyecto
    def devolver_info_persona(self):
        print("--> \n  Nombre : " + self.nombre_persona )
        print("  ID : "+ self.ID)
        print("  Edad : " + str(self.edad) )
        print("  Profesion : " + self.profesion )



#-------------------------------------------------------------------------------------
#PRUEBA DE ESCRITORIO DE CODIGO CON BASE EN POO
#La idea es poner a prueba la creacion de objetos con base en las clases ya creadas

#Se crea vector para almacenar las personas que hacen parte del proyecto 1 y proyecto 2 respectivamente
personas_involucradas_1 = []
personas_involucradas_2 = []

#Se agregan tantas personas como sea necesario al proyecto 1 y 2 (sus participantes directos)...
#...notar que el vector NO es matriz, sino que es vector de OBJETOS!!!!
#...Es fundamental tener claro esto, para luego poder acceder a info y organizacion de jerarquias
personas_involucradas_1.append( Persona("Juan Guillermo Rodriguez", 20,"Ingeniero Sistemas","111") )
personas_involucradas_1.append( Persona("Santiago Garcia Arango", 20,"Ingeniero Mecatronico","222") )
personas_involucradas_1.append( Persona("Monica Hill Donadio", 22,"Ingeniero Financiero","333") )
personas_involucradas_1.append( Persona("Felipe Alvarez Jaramillo", 25,"Tecnico Sistemas","444") )
personas_involucradas_1.append( Persona("Alejandro Castanno Posada", 22,"Practicante","555") )

personas_involucradas_2.append( Persona("Santiago Garcia Arango", 20,"Ingeniero Mecatronico","222") )
personas_involucradas_2.append( Persona("Manuela Medina Gomez", 24,"Ingeniera Industrial","888") )
personas_involucradas_2.append( Persona("Jaime Ramirez Ospina", 30,"Administrador","666"))
personas_involucradas_2.append( Persona("Gabriela Martinez Posada", 22,"Contadora","777") )
personas_involucradas_2.append( Persona("Monica Hill Donadio", 22,"Ingeniero Financiero","333") )
personas_involucradas_2.append( Persona("Daniela Ruiz Yepes", 29,"Ilustradora","999") )
personas_involucradas_2.append( Persona("Esperanza Toro Gaviria", 26,"Secretaria","000") )

#Se crean proyectos, teniendo en cuenta las personas involucradas
p1 = Proyecto("Pagina Web Dejando Huella Fertilidad", personas_involucradas_1, "15/01/2020",1000000 )
p2 = Proyecto("Desarrollo de Algoritmos Financieros para Trading", personas_involucradas_2, "15/01/2020",1500000)

#Se accede a metodo interno de proyectos creados y de esta forma se obtiene info total del proyectos
p1.devolver_info()
p2.devolver_info()

#Nota... si queremos aplicar "print" a objetos, ver lo que sucede en terminal al correr...
#se obtiene algo tipo "<__main__.Proyecto objecto at 0x00000012938D2B0>", es decir, un identificador interno de python
print(p1)
print(p2)
#Por lo tanto, se deben crear metodos "__str__" y "__repr__" para que "print" devuelva lo que queramos