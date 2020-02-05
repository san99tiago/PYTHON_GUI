#Santiago Garcia Arango, 16 Enero 2020
#MANEJO SENCILLO DE BOTONES Y "ENTRY" EN TKINTER
#------------------------------------------------------------------------
#Es fundamental tener widgets interactivos para el programa, como los botoes y entry fields.
#Ambos se deben crear primero y luego posicionar por alguno de los dos sistemas (grid/pack)

#------------------------------------------------------------------------
#EJEMPLO:
#Se crea aplicacion sencilla con dos botones, que ambos hacen algo

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se crea ventana principal, nombrada por nosotros "root"
root = tk.Tk()

#Se crea label encargada de indicar que el usuario ingrese el nombre
texto_1 = ttk.Label( root, text = "Ingrese su nombre: " )
texto_1.grid(row =0, column =0 )

#Se crea label para luego interactuar con ella al tocar boton
texto_2 = ttk.Label( root, text = " " )
#Nota: columnspan o rowspan permiten hacer widgets de "grosor" de N columas o filas
texto_2.grid(row =1, column =0,columnspan = 3 )

#Se crea Entry Field (para ingresar info por el usuario)
#FUNDAMENTAL: crear "tk.StringVar()" para manejo de Entry fields
nombre_usuario = tk.StringVar()
entrada = ttk.Entry( root,width = 20, textvariable = nombre_usuario )
entrada.grid( row = 0, column =1 )
#OJO: truco interesante: hacer que el usuario ya tenga el "mouse" listo para escribir:
entrada.focus()

#Se crean dos botones, uno para imprimir algo en terminal y otro para salirse
#WARNING: "command" permite hacer funcion al tocar boton, pero NO se pone entre parentesis...
#... de lo contrario NO funcionaria al tocarla, sino al inicializar...
#NOTA: Se debe crear funcion del boton, antes de crearlo

def funcion_tocame():
    #Se cambia texto de label, con ayuda de "condigure()"
    #Ver forma de obtener info de Entry asociado al nombre...
    #...es a traves de la variable "nombre_usuario", llamando a "get()"
    texto_2.configure( text = "Gracias por tocarme {}".format(nombre_usuario.get()) )

b_1 = ttk.Button( root, text = "TOCAME" , command = funcion_tocame)
b_1.grid(row =0, column = 2, padx = (10,50))
#Mirar padx como "padding en x externo"
#Tambien existe ipadx comom "internal padding en x"

b_2 = ttk.Button(root, text = "SALIR", command = quit)
b_2.grid(row = 0, column = 3)

#Se ejecuta finalmente toda la ventana de tkinter con el mainloop()
root.mainloop()

