#Santiago Garcia Arango, 17 Enero 2020
#MANEJO DE TKINTER MAS AVANZADO, CON PROGRAMACION ORIENTADA A OBJETOS
#------------------------------------------------------------------------
'''
El objetivo de esta etapa es aprender a manejar correctamente Tkinter con ayuda
de las herramientas y logica enfocada a la Programacion Orientada a Objetos.
Esto nos permitira crear aplicaciones con mayores profundidades y capacidades,
manteniendo un orden basado en clases.
Ademas, se explicara la forma de aprovechar la herencia de Tkinter, para manejar
lo que habiamos manejado como "root", ahora como la clase principal, y las otras
clases seran las encargadas de llevar la info de las otras "ventanas" de la app.

'''
#------------------------------------------------------------------------

#Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
#SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se crea clase que reemplaza/genera el mismo efecto del "root", asi:
#Aprovechandonos de la herencia, al crear la clase, se hereda de tk.Tk, esto...
#... tendra grandes beneficios, porque:
#1. Se agrega funcionalidades y variables internas a la clase, que tk.Tk NO tienen.
#2. Al llamar a algo que sea directamente de tk.Tk, lo busca en APP, y luego lo busca en tk.Tk...
#...permitiendo facilitar el uso de esta funcionalidad de tkinter y a la vez, tener metodos/atributos extras.
class APP(tk.Tk):
    def __init__(self):
        #OJO: Se debe inicializar no solamente APP, sino la inicializacion de tk.Tk, para garantizar la inicializacion...
        #... correcta de de tkinter y su respectiva funcion "Tk".
        #Notar que antes haciamos root = tk.Tk() , ahora se hace lo mismo, a traves de inicializar la clase (mismo proceso).
        #Esto nos permitira almacenar todo en la APP, con ventajas enormes, que veremos mas adelante
        super().__init__()
        #NOTA: Esta inicializacion con super() --> de herencia de tk.Tk, es exctamente lo mismo que decir:
        #... self = tk.Tk()
        #... la razon de esto es porque toda inicializacion que pase en objeto, se procesa en "self"!!!
        # es decir, de ahora en adelante, self se puede ver como la misma ventana que siempre hemos llamado root = tk.Tk()

        #Ahora, aprovechandose de esta herencia e inicializacion, se puede llamar self.________ como si self fuera root.
        self.title("TEST")
        self.state("zoomed")
        
        L1 = tk.Label( self, text = "PRIMER LABEL EN VENTANA CON POO APLICADA", font = ("Times New Roman",14,"bold"), bg = "#00FFFF",fg = "blue")
        L1.pack(expand = True, fill = "both")



#Se crea clase... (a la vez se esta creando la ventana asociada, gracias a la herencia de tk.Tk)
#NOTA: luego de crear clase, tambien se pueden ejecutar funciones de tk.Tk, como  se ve abajo (por si se necesita, es bueno saberlo)
root = APP()
root.resizable(0,0)

#se ejecuta el maniloop para que APP (que contiene toda la info de tk.Tk(), corra correctamente y se muestre ventana con info)
root.mainloop()