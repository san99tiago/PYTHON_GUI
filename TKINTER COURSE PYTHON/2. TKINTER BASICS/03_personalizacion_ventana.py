#Santiago Garcia Arango, 16 Enero 2020
#PERSONALIZACION VENTANA
#IMAGENES, TITULO, ICONOS, TAMANNO
#------------------------------------------------------------------------

#Se muestra forma sencilla de agregarle titulo a la ventana y el icono deseado
#NOTA: para el icono, se debe tener el archivo en formato ".ico"

#------------------------------------------------------------------------

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Es util-para indicar el path cuando trabajemos con "png", "jpg"y "ico"
import os

#SI QUEREMOS TRABAJAR CON IMAGENES
#(OJO: se debe descargar libreria, recomndado descargarlas con: "pip install pillow" )
#Esta libreria es muy importante, porque es la manera mas sencilla de usar imagenes
from PIL import ImageTk, Image


#--------------------------------COMIENZA LA CREACION DE LA VENTANA DE TRABAJO----------------------------------

#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("PERSONALIZACION VENTANA TKINTER")

#Se agregan las dimensiones deseadas de la ventana de trabajo
root.geometry( "1000x500" )

#Se agrega el icono de la ventana de trabajo, el cual tambien se indica en la parte superior a la izquierda
#...se debe tener el icono en formato "ico" en la misma carpeta de trabajo (sino, indicar path absoluto)
root.iconbitmap( "{}\\ICON_2.ico".format( os.getcwd() ) )


#AGREGAR IMAGENES... (con libreria PIL)
#... se crea formato interno de imagen (path puede variar)
#OJO, proceso tambien incluye redimensionar la imagen a los pixeles deseados, en este caso a con redondeo del porcentaje total de la pantalla...(con Image.ANTIALIAS)
# img_1 = ImageTk.PhotoImage( Image.open("FOTO_1.jpg").resize( (math.floor(w*0.1),math.floor(h*0.2)),Image.ANTIALIAS ) )
img_1 = ImageTk.PhotoImage( Image.open("FOTO_1.jpg").resize( (500,200),Image.ANTIALIAS ) )

#Se crea la imagen sobre widget de Label, con parametro "image"
cuadro_img_1 = tk.Label( root, image = img_1 )
#Se agrega visualmente en el grid o lugar donde se desee mostrar
cuadro_img_1.grid( column = 0, row = 0)



#Dropdown menus...
#Se debe crear variable asociada al menu respectivo...(para indicar elegido respectivo)
elegido_menu_1 = tk.StringVar(root)
elegido_menu_1.set("ELEGIR PROYECTO")

#Se crea el menu y luego se coloca en root...
#...OJO: CREAR MENU A PARTIR DE VECTOR:
VECTOR = []
for i in range( 50 ):
    VECTOR.append( str(i+1) + ". PROYECTO ALGO" )
#TRUCO: importar modulo ttk desde tkinter (ver al inicio), para tener un dropdownmenu mucho mejor y que tenga scrollbar (en caso de ser muchos proyectos)
menu_1 = ttk.Combobox( root, textvariable = elegido_menu_1, values = VECTOR )
menu_1.grid(row = 1, column = 3)



#Se ejecuta el "mainloop" que permite correr el codigo de la ventana correctamente
root.mainloop()



