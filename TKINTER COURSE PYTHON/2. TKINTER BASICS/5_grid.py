#Santiago Garcia Arango, 16 Enero 2020
# SE TRABAJA CON FORMA DE ORGANIZAR GUI TIPO GRID
#-------------------------------------------------------------------------------
#GRID: es como una matriz interna compuesta por filas y columnas
#Este GRID hace que sea mas sencillo organizar proyectos visuales a nivel matricial
#Se pueden modificar "grosores" de widgets, para que ocupen 1,2,N columnas o filas
#Se facilita mucho el trabajo con esta forma de organizacion. Es la mejor.
#NOTA: Tambien es util trabajar con Frames dentro del grid()

#IMPORTANTE:
#Hacer que columna o fila "N" tenga un peso de 1, es decir, que se lleve el espacio...
#...maximo, relativo de "1", con respectos a las otras columnas.
#tener en cuenta que por defecto, el peso es 0 para todas las columnas/filas.
#Tambien se puede configurar que el peso sea 2,3,4,etc...
#OJO: esto nos permite que al expandir programa, se expanda la columna/fila correctamente
#root.columnconfigure( N , weight = 1)
#root.rowconfigure( N , weight = 1)


#-------------------------------------------------------------------------------
#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("GRID")

#Se da un color de fondo predeterminado
root.configure( bg = "black" )

#Se configuran todas las columnas de trabajo con mismo peso, para facilidad al expandir
root.columnconfigure( 0, weight =1 )
root.columnconfigure( 1, weight =1 )
root.columnconfigure( 2, weight =1 )
root.columnconfigure( 3, weight =1 )
#Forma cool rapida de hacerlo: (a traves de tupla)
root.columnconfigure( (0,1,2,3), weight =1 )



#Se creea label para indicar que es la fila cero
#OJO: Ver "columnspan", para indicar que este widget ocupa multiples columnas
#OJO: ver color indicado de forma HEX
#OJO: ver "sticky" como forma de llevar fondo completo al tamanno del widget (north,south,east,west)
texto_0 = tk.Label( root, text = ".........ESTA ES LA FILA CERO..........",bg = "#00FFFF" )
texto_0.grid(row =0, column =0, columnspan = 4 , sticky = "nsew")

#Se crea label encargada de indicar que el usuario ingrese el nombre
texto_1 = tk.Label( root, text = "Ingrese su nombre: ", bg = "black", fg = "white" )
texto_1.grid(row =1, column =0 )

#Se crea label para luego interactuar con ella al tocar boton
texto_2 = tk.Label( root, text = " ", bg = "black", fg = "yellow" )
#Nota: columnspan o rowspan permiten hacer widgets de "grosor" de N columas o filas
texto_2.grid(row =2, column =0,columnspan = 3 )

#Se crea Entry Field (para ingresar info por el usuario)
#FUNDAMENTAL: crear "tk.StringVar()" para manejo de Entry fields
nombre_usuario = tk.StringVar()
entrada = ttk.Entry( root,width = 20, textvariable = nombre_usuario )
entrada.grid( row = 1, column =1 , sticky = "ew")
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

#Importante: si queremos que boton "se agrande/amplie" con expandir ventan, aplicar "sticky"
b_1 = ttk.Button( root, text = "TOCAME" , command = funcion_tocame)
b_1.grid(row =1, column = 2, padx = (10,30), sticky = "ew")
#Mirar padx como "padding en x externo"
#Tambien existe ipadx comom "internal padding en x"

b_2 = ttk.Button(root, text = "SALIR", command = quit)
b_2.grid(row = 1, column = 3)







#Se ejecuta ventana que corre tkinter para funcionar correctamente
root.mainloop()




