#Santiago Garcia Arango, 16 Enero 2020
#BASICOS 1 DE TKINTER
#------------------------------------------------------------------------
#Tkinter es una libreria basada en tcl, que permite facilitar el desarrollo...
#...de aplicaciones "GUI", es decir, Graphical User Inteface
#Esta libreria ya viene instalada en el computador por defecto
#Ademas, trabajaremos con una opcion de tkinter, llamada ttk, la cual...
#...nos permitira obtener mas estilos, opciones y personalizaciones

#NOTA:
#La forma de agregar "widgets" en tkinter es a traves de dos pasos siempre:
#1--> Crear la esencia del objeto y sus caracteristicas, inluyendo su 'parent'
#2--> Posicionarlo a traves de sistema de organizacion visualj: hay dos-->(grid o pack)
#Ademas se puede realizar esto en una misma linea, o en dos (yo prefiero en dos por el orden)


#-----------------------------------------------------------------------
#Se importan las librerias mencionadas
import tkinter as tk
from tkinter import ttk

#Se crea la "ventana principal", a veces llamada "root".
#Nota: esta ventana NO corre, hasta llamar a "root.mainloop()" (con esto se ejecuta)
root = tk.Tk()

#Forma sencilla de agregar un texto/label a la ventana principal (porque se agrega al "root")
#Nota: se puede agregar a diferentes "Frames", o "contenedores" (mas adelante)
#al indicar el root, se esta diciendo que el "parent" del widget es root y ahi se debe posicionar
mi_texto_1  =ttk.Label(root,text = "HOLA, LA DISCIPLINA TARDE O TEMPRANO VENCERA LA INTELIGENCIA")
#Luego de crear la esencia de mi texto, se agrega visualmente a la ventana...
#nota: por ahora lo haremos con "pack()", porque es mas sencillo, luego se hara...
#... con grid() y quedara mucho mas organizado y personalizado
#OJO: en caso de ser necesario, se puede editar mas cosas del widget creado asi:
#(agregarmos "padding" que es una tupla para modificar tamannos de separacion de lados vert. y horiz.
#NOTA (esto tambien se puede hacer en la creacion del widget (o en widget.configure() )  )
mi_texto_1.configure( padding =( 50,10 ) )
mi_texto_1.pack()


#Se crea automaticamente la ventana con todas las especificaciones aqui.
#NOTA: aqui se queda el codigo de Python corriendo indefinidamente (hasta salir de ventana)
root.mainloop()
