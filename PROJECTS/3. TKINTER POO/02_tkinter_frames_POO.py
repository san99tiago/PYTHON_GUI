#Santiago Garcia Arango, 17 Enero 2020
#MANEJO DE TKINTER MAS AVANZADO, CON PROGRAMACION ORIENTADA A OBJETOS (FRAMES)
#COOL: poder hacer que al presionar "Enter", suceda algo (lo que sea)
#------------------------------------------------------------------------
'''
Luego de ver codigo "1", con explicacion de metodologia para POO con tkinter,
se continua metodologia para extender a nuevos Frames en tkinter con POO.
IMPORTANTE:
Recordemos que los Frames siempre tienen una estructura de este tipo:
F = tk.Frame( root )
Es decir, esto nos dice dos cosas importantes a tener en cuenta al crear frames con POO:
1. Nuestros Frames creados en clases, deberan heredar todo desde tk.Frame
2. Nuestros Frames creados en clases, deben recibir como parametros, un "contenedor",
el cual es llamado normalmente root, pero puede ser realmente otros frames tambien.
Estos dos puntos se explican abajo en el ejemplo practico de estas cosas a tener en cuenta

'''
#------------------------------------------------------------------------
#EJEMPLO: Se crea app con explicacion de Frames, basandose en POO


#Se ejecuta intento de trabajar ventanas en HD, solo disponible en Windows (por eso el "try-except")
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

#Siguiendo info del codigo anterior, se ejecuta igualmente... (si no se entiende ver codigo para explicacion)
class APP(tk.Tk):
    #OJO: Notar que pasamos "*args" y "**kwargs", porque podrian ser necesarios (recordar pasarlos a inicializacion de tk.Tk)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Se aprovecha que "self" ya es la ventana principal y se agrega titulo respectivo
        self.title("TKINTER CON FRAME Y POO")
        
        #Se busca que Ventana se mantenga central y correcta a traves de:
        self.columnconfigure( 0, weight = 1 )


        #Se crea Frame_1, la cual debemos logicamente, indicar donde se debe posicionar (en este caso en self, osea "root")
        #OJO: Recordar que no solamente se crea, sino que se debe posicionar (en este caso con pack()  )
        self.F_1 = Frame_1( self )
        self.F_1.pack(expand = True, fill = "both")


        #FORMA DE DAR FUNCION DEL BOTON, CON ENTER, SIEMPRE COLOCAR "bindings" en ROOT (tk.Tk)
        #IMPORTANTE: Al agregar bindings (acciones como las de enter), SE EXIGE AGREGAR "*args" a funcion, para que entienda el evento...
        #... gracias la funcion, con parametros disponible, de lo contrario, no funciona el enter como comando de activacion
        #Este bind es para llamar a funcion "saludarme", ubicada en clase de F_1, como metodo (encargado de cambiar Label) al presionar "Enter"
        self.bind( "<Return>", self.F_1.saludarme )
        #Este bind es para llamar a funcion "saludarme", ubicada en clase de F_1, como metodo (encargado de cambiar Label) al presionar "Enter Numerico"
        self.bind( "<KP_Enter>", self.F_1.saludarme )







#OJO( CREACION DE FRAMES):
#Se crean como clases con herencia de tk.Frame (para acceder inmediatamente a la clase Frame)
#NOTA: Si bien creamos Frame, recordemos que hace falta "llamarla", de lo contrario, no se crea ni se hace efectiva
class Frame_1(tk.Frame):
    #Se inicializan, recibiendo de parametro self y container (el container es en donde esta ubicado el Frame)
    #Recordemos que este container sera entonces un parametro que debemos incluir, al llamar a clase.
    #Se pueden incluir los *args y **kwargs, como parametros extra disponibles
    def __init__(self, container,*args, **kwargs):
        #Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        #NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        #Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow", padx = 50, pady = 10 )

        #Agregamos Widgets, con la ventaja de poder agregarlos en "self"(Frame_1)-->tk.Frame , que a su vez, estara en root(APP)-->tk.Tk
        #Variable para texto del usuario, el objetivo es poder obtener la info de Entry (E_1)
        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI PRIMER FRAME CON POO Y TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Ingrese Nombre: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        E_1.focus()
        E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))


        #OJO: mirar B_1, es boton, que su command activa un metodo interno de la clase. Esto es maravilloso.
        #esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button( self, text = "SALUDARME" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

 
        #OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")



    #OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Hola {}.".format( self.entrada_usuario.get() ) )


#Se crea APP como tal (aprovechandonos de la clase creada)
root = APP()

#Cambiar "font" por defecto a todo (ojo con forma de importar libreria arriba)
font.nametofont("TkDefaultFont").configure(size = 12, underline = True)

#Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
root.mainloop()