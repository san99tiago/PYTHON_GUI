#Santiago Garcia Arango, 17 Enero 2020
#SE CREAN COMBOBOXES
#----------------------------------------------------------------------------------------
#Son los menus desplegables, que a su vez nos indican info importante de lo seleccionado...
#...por el usuario. Es importante crearlas y acceder a lo que tienen en todo momento.
#Ver codigo para entender funcionamiento

#----------------------------------------------------------------------------------------
#EJEMPLO:
#Programa que maneja 2 comboboxes al tiempo, donde la info del segundo depende de la seleccion del primero
#Luego, se obtiene info de ambos combobox y se muestra eleccion usuario en terminal
#IMPORTANTE VER FORMA DE OBTENER INFO DE SELECCION COMBOBOX...
#IMPORTANTE ENTENDER COMO EJECUTAR ACCION AL SELECCIONAR OPCION DE COMBOBOX...
#IMPORTANTE VER COMO RESETEAR VALOR POR DEFECTO (NULO) DE COMBOBOX.

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
#SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Se crea ventana principal
root = tk.Tk()

#Se agrega titulo, geometria y Evitar redimensionar
root.title("COMBOBOXES")
root.geometry("1200x700")
root.resizable(0,0)

#Se agrega estilo de labels
font = ("Verdana",12)

#Se debe crear variable para manejo de inifo seleccionada en combobox 1 y combobox 2
#Siempre que se quiera acceder a esta variable (asociada a la seleccion), se debe llamar...
#... a seleccion_combobox_1.get()   o     seleccion_combobox_2.get()
seleccion_combobox_1 = tk.StringVar( root )
seleccion_combobox_2 = tk.StringVar( root )


#Se crea texto para indicar lo que se debe elegir en combobox 1 y 2
texto_1 = tk.Label( root, text = "Elija el barrio donde vive: " ,font = font)
texto_1.grid(row=0,column=0, sticky = "w")
texto_2 = tk.Label( root, text = "Elija su CC favorito del barrio: ", font = font )
texto_2.grid(row=1,column=0,sticky = "w")

#Se crea combobox 1
vector_barrios = ["Poblado","Laureles","Belen","Envigado"]
menu_barrios = ttk.Combobox( root, textvariable = seleccion_combobox_1, values = vector_barrios, state = "readonly" )
menu_barrios.grid(row = 0, column = 1)


#Se crea combobox 2
menu_cc = ttk.Combobox( root, textvariable = seleccion_combobox_2, values = [], state = "readonly" )
menu_cc.grid(row = 1, column = 1)

#Se crea funcion que se encarga de manejar el item elegido en combobox 1
#Siempre colocar "event"...
#OJO: SIEMPRE que se desee llamar funcion al seleccionar info de combobox, se llama asi:
#... NombreCombobox.bind("<<ComboboxSelected>>", NombreFuncionARealizar)  ---> ojo: llamar luego de definir funcion, sino es error
def modificar_combobox_2(event):
    #Se obtiene nombre de lo que se encuentra seleccionado actualmente en combobox1
    seleccion = seleccion_combobox_1.get()
    #Se agregan opciones del combobox 2 para que usuario pueda elegir segun primera eleccion de combobox 1
    if seleccion == "Poblado":
        menu_cc.config( values = ["Santafe","Oviedo","El Tesoro","Sandiego","La Visitacion","Del Este"] )
        #OJO: de esta forma que evita que info erronea quede seleccionada en combobox (clear seleccion de combobox2)
        menu_cc.set("")
    elif seleccion == "Laureles":
        menu_cc.config( values = ["Viva Laureles","Unicentro","La 70 Mall","Mall Laureles"] )
        #OJO: de esta forma que evita que info erronea quede seleccionada en combobox (clear seleccion de combobox2)
        menu_cc.set("")

    elif seleccion == "Belen":
        menu_cc.config( values = ["La Mota","Granvia Mall","Los Molinos","Mall Belen","Arkadia","Belensito Mall"])
        menu_cc.set("")

    elif seleccion == "Envigado":
        menu_cc.config( values = ["Viva Envigado","La Frontera Mall","Sao Paulo","Parque Envigado","Mall San Lucas","City Plaza"] )
        menu_cc.set("")

#OJO: ESTO DE ACA ABAJO ES LA MAGIA DE HACER ALGO AL SELECCIONAR...
#SIEMPRE QUE SE CREE FUNCION, SE INDICA QUE EL COMBOBOX REALIICE LA FUNCION ASI:
menu_barrios.bind( "<<ComboboxSelected>>",modificar_combobox_2 )


#Ahora creamos funcion que funcione al seleccionar combobox2, como registro de info total (de ambos)
def mostrar_info_al_seleccionar_combobox_2(event):
    #Se valida que el usuario haya elegido algo nuevo en combobox 2 (diferente a nulo)
    if menu_cc.current() != -1:
        #Se muestran dos formas de obtener info (una es seleccion y otra es index o posicion asociada al vector inicial de valores)
        seleccion_1 = seleccion_combobox_1.get()
        seleccion_1_index = menu_barrios.current()
        
        seleccion_2 = seleccion_combobox_2.get()
        seleccion_2_index = menu_cc.current()

        #Se elimina lo seleccionado en ambos combobox, para que no queden mostrandose erroneamente
        menu_cc.set("")
        menu_barrios.set("")
        #Se resetean las opciones del combobox2 a nulas
        menu_cc.config( values = [] )
        #Se devuelve la info total de lo elegido por el usuario al elegir segundo combobox
        print("\nSELECCION USUARIO: ")
        print(" {}({}) __ {}({})".format( seleccion_1,seleccion_1_index,seleccion_2,seleccion_2_index ))
#RECORDAR QUE ESTAS FUNCIONES SOLO CORREN SI SE DEFINE LA ACCION AL SELECCIONAR INFO (ASI:)
menu_cc.bind("<<ComboboxSelected>>",mostrar_info_al_seleccionar_combobox_2)


#Se ejecuta ventana de trabajo
root.mainloop()
