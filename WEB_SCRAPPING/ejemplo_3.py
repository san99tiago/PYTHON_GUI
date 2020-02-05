#Santiago Garcia Arango, Febrero 5 de 2020
#CONTINUACION APRENDIZAJE WEB SCRAPPING
#-----------------------------------------------------------
#SIMPLE APP PARA PODER OBTENER EL PRECIO DE LA TRM
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import date

class APP_TRM:
    def __init__(self):
        pass

    #METODO PARA OBTENER TRM DE INTERNET
    def obtener_TRM(self):
        #Se ingresa link de pagina web a revisar
        url_1 = 'https://www.trmhoy.co/'

        #Se ejecuta comando para hacer el request a la pagina web indicada
        pagina_obtenida = requests.get(url_1)

        #Se verifica que haya sido exitoso el request realizado previamente
        #codigo de estado correcto = 200 
        # INFO_1_codigo_estado = pagina_obtenida.status_code

        #Accedemos a parsear informacion obtenida con metodo "lxml" del texto
        sopa_1 = BeautifulSoup( pagina_obtenida.text , "lxml" )

        #Buscamos referencias deseadas asociadas al lugar donde indican el precio de TRM
        #recordar: esto se hace inspeccionando pagina web y su estructura html
        #al encontrar "div" en estrucutra, con id:banner-wrapper, se procede a acceder...
        #...a "h2", que es el que contiene el precio del TRM
        TRM = sopa_1.find( "div", attrs = {"id":"banner-wrapper"} )
        TRM = TRM.h2.get_text()
        print(TRM)
        return(TRM)


#CREACION CLASE PARA MANEJO DE TRM
MANEJO_TRM = APP_TRM()
#APP PARA VISUALIZAR INFO DE TRM SENCILLA
root = tk.Tk()
root.title("TRM HOY")
INFO_1 = tk.Label(root, text = "{} {}".format("Fecha actual: ", date.today() ), font = ["Times New Roman",16,"bold"] )
INFO_1.grid(row = 0, column = 0, columnspan = 2, pady = (10,20))

INFO_2 = tk.Label(root, text = "TRM DE HOY: ", font = ["Times New Roman",14])
INFO_2.grid(row = 1, column = 0, padx = (0,10),pady = (0,50))

INFO_3 = tk.Label(root, text = MANEJO_TRM.obtener_TRM() , font = ["Times New Roman",14], bg = "green")
INFO_3.grid(row = 1, column = 1, padx = (0,50),pady = (0,50))


root.mainloop()