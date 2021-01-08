#ALGORITMO PARA INTERFAZ DE EMPALME TIPO ESPIRAL
#Desarrollado por:
# Camila Martinez, Santiago Garcia, Esteban Medina
# Marzo 2020

#Se importan las librerias mencionadas
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import math

#Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
#(Correr esta linea de codigo al inicio)
#SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


#Se agrega estilos sencillos para los fonts del programa
font_1 = ("Verdana",12,"bold")
font_2 = ("Verdana",10,"bold")
font_3 = ("Verdana",10)

#Se crea la "ventana principal", a veces llamada "root".
#Nota: esta ventana NO corre, hasta llamar a "root.mainloop()" (con esto se ejecuta)
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("TRABAJO SANTIAGO GARCIA")

#Se da un color de fondo predeterminado
root.configure( bg = "black" )

#Se agregan widets al root (ventana de interfaz)
#Titulo de la interfaz
TITULO = tk.Label( root, text = "ALGORITMO ESPIRAL EN S", bg = "black",fg = "yellow", font = font_1)
TITULO.grid(row =0, column =0, columnspan = 4 , sticky = "nsew",pady = (10,0), padx = (10,10))

#Titulo para el ingreso
label_ingreso = tk.Label( root, text = "Ingrese los siguientes parametros: ", bg = "black",fg = "white", font = font_2)
label_ingreso.grid(row =1, column =0, columnspan = 2,sticky = "w", pady = (15,10),padx = (10,0))


#Entradas del algoritmo

label_R1 = tk.Label( root, text = "Ingrese valor de 'R1':  ", bg = "black",fg = "white", font = font_3)
label_R1.grid(row =2, column =1, sticky = "w")

label_R2 = tk.Label( root, text = "Ingrese valor de 'R2':  ", bg = "black",fg = "white", font = font_3)
label_R2.grid(row =3, column =1, sticky = "w")

label_D_M = tk.Label( root, text = "Elegir ingreso de 'D' o 'M':  ", bg = "black",fg = "white", font = font_3)
label_D_M.grid(row =4, column =1, sticky = "w")

label_D_M = tk.Label( root, text = "Ingrese valor de 'D' o 'M':  ", bg = "black",fg = "white", font = font_3)
label_D_M.grid(row =5, column =1, sticky = "w")

#Ingreso de valores de entrada
#Se crea Entry Field (para ingresar info por el usuario)
#FUNDAMENTAL: crear "tk.StringVar()" para manejo de Entry fields y sus variables

R1 = tk.StringVar()
entry_1 = ttk.Entry( root,width = 25, textvariable = R1 )
entry_1.grid( row = 2, column =2, sticky = "ew" )
R1.set(120)

R2 = tk.StringVar()
entry_2 = ttk.Entry( root,width = 25, textvariable = R2 )
entry_2.grid( row = 3, column =2, sticky = "ew" )
R2.set(100)

entry_3 = ttk.Combobox( root,width = 25, values = ["D","M"], state = "readonly" )
entry_3.grid( row = 4, column =2, sticky = "ew" )

D_M = tk.StringVar()
entry_4 = ttk.Entry( root,width = 25, textvariable = D_M )
entry_4.grid( row = 5, column =2, sticky = "ew" )


#Titulo para las salidas
label_salida = tk.Label( root, text = "Los valores obtenidos son: ", bg = "black",fg = "white",font = font_2)
label_salida.grid(row =7, column =0, columnspan = 2,sticky = "w", pady = (15,10),padx = (10,0))

#Salidas del algoritmo 
label_info_M2 = tk.Label( root, text = "M^2: ", bg = "black",fg = "white", font = font_3)
label_info_M2.grid(row =8, column =1, sticky = "ew")

label_resultadoM2 = tk.Label( root, text = " ", bg = "black",fg = "white", font = font_3)
label_resultadoM2.grid(row =8, column =2, sticky = "ew")


#--- Nueva salida, agregado:

label_infoLE1 = tk.Label( root, text = "Le1: ", bg = "black",fg = "white", font = font_3)
label_infoLE1.grid(row =9, column =1, sticky = "ew")

label_resultadoLE1 = tk.Label( root, text = " ", bg = "black",fg = "white", font = font_3)
label_resultadoLE1.grid(row =9, column =2, sticky = "ew")

label_infoLE2 = tk.Label( root, text = "Le2: ", bg = "black",fg = "white", font = font_3)
label_infoLE2.grid(row =10, column =1, sticky = "ew")

label_resultadoLE2 = tk.Label( root, text = " ", bg = "black",fg = "white", font = font_3)
label_resultadoLE2.grid(row =10, column =2, sticky = "ew")

label_infoM1 = tk.Label( root, text = "M: ", bg = "black",fg = "white", font = font_3)
label_infoM1.grid(row =11, column =1, sticky = "ew")

label_resultadoM1 = tk.Label( root, text = " ", bg = "black",fg = "white", font = font_3)
label_resultadoM1.grid(row =11, column =2, sticky = "ew")







#Se crea boton que ejecuta el codigo principal del programa
#WARNING: "command" permite hacer funcion al tocar boton, pero NO se pone entre parentesis...
#... de lo contrario NO funcionaria al tocarla, sino al inicializar...
#NOTA: Se debe crear funcion del boton, antes de crearlo


def funcion_tocame():
    #OPERACIONES NECESARIAS PARA OBTENER M2
    if ( R1.get() == "" or R2.get() == "" or D_M.get() == "" or entry_3.current() == -1 ):
        showinfo( "ERROR DE DATOS", "Ingrese datos correctamente" )

    else:
        R1_AUX = float( R1.get() )
        R2_AUX = float( R2.get() )

        if entry_3.current() == 0:
            #USUARIO INGRESO VALOR DE 'D'
            D_AUX = entry_4.get()
            

            Q=1
            cont=0

            M = float ( entry_4.get() ) + R1_AUX + R2_AUX
            R = (R1_AUX * R2_AUX) / (R1_AUX + R2_AUX)
            
        
            while (Q) > 0.001 and cont < 1000:

                 cont = cont + 1
            
                 D_AUX =  M - (R1_AUX + R2_AUX)

                             
                 Aw = ( 24*D_AUX*(R**3) )**(1/4)
                 
                 Le2 = (Aw)/(R2_AUX)
            
                 Le1 = (Aw)/(R1_AUX)


                 T1 = (( (Le1)*(90) )/( (R1_AUX) * math.pi ))*(math.pi)/180
            
                 Xe1=(Le1)*(1 - (T1**2)/10 + (T1**4)/216 - (T1**6)/9360  + (T1**8)/685440 )

                 XM1 = Xe1 - (R1_AUX)*( math.sin( T1 ) )

                 DR1 = (Le1**2)/(24*R1_AUX)

                 YM_1 = R1_AUX + DR1



                 T2 = (( (Le2)*(90) )/( (R2_AUX) * math.pi ))*(math.pi)/180

                 Xe2=(Le2)*(1 - (T2**2)/10 + (T2**4)/216 - (T2**6)/9360  + (T2**8)/685440 )

                 XM2 = Xe2 - (R2_AUX)*( math.sin( T2) )     

                 DR2 = (Le2**2)/(24*R2_AUX)

                 YM_2 = R2_AUX + DR2



                 SUM_Y = YM_1 + YM_2

                 SUM_X= XM1 + XM2


                 M2= (SUM_X)**2 + (SUM_Y)**2
                
                        
                 M= float ( math.sqrt(M2) )

                  

                 if math.sqrt(M2) != M:
                     M = math.sqrt(M2)

                 if math.sqrt(M2) == M:
                     Q=1
                 else: 
                     Q= abs(M-math.sqrt(M2))
          
            VARIABLE_M_2 = str(  float (M2)  )
            VARIABLE_M_3 = str( float (Le1)  )
            VARIABLE_M_4 = str( float (Le2)  )
            VARIABLE_M_5 = str( float (math.sqrt(M2))  )
        
        else:

            if float(D_M.get()) < float( R1.get() ) + float ( R2.get() ):
                showinfo( "ERROR DE DATOS", "El valor de M no puede ser menor que la suma de los radios" )
            else:
                #USUARIO INGRESO VALOR DE 'M'
                M = float (entry_4.get())
                R = (R1_AUX * R2_AUX) / (R1_AUX + R2_AUX)
                
                Q=1
                cont=0
            
                while (Q) > 0.001 and cont < 1000:

                    cont = cont + 1
                
                    D_AUX =  M - (R1_AUX + R2_AUX)

                                
                    Aw = ( 24*D_AUX*(R**3) )**(1/4)
                    
                    Le2 = (Aw)/(R2_AUX)
                
                    Le1 = (Aw)/(R1_AUX)


                    T1 = (( (Le1)*(90) )/( (R1_AUX) * math.pi ))*(math.pi)/180
                
                    Xe1=(Le1)*(1 - (T1**2)/10 + (T1**4)/216 - (T1**6)/9360  + (T1**8)/685440 )

                    XM1 = Xe1 - (R1_AUX)*( math.sin( T1 ) )

                    DR1 = (Le1**2)/(24*R1_AUX)

                    YM_1 = R1_AUX + DR1



                    T2 = (( (Le2)*(90) )/( (R2_AUX) * math.pi ))*(math.pi)/180

                    Xe2=(Le2)*(1 - (T2**2)/10 + (T2**4)/216 - (T2**6)/9360  + (T2**8)/685440 )

                    XM2 = Xe2 - (R2_AUX)*( math.sin( T2) )     

                    DR2 = (Le2**2)/(24*R2_AUX)

                    YM_2 = R2_AUX + DR2



                    SUM_Y = YM_1 + YM_2

                    SUM_X= XM1 + XM2


                    M2= (SUM_X)**2 + (SUM_Y)**2
                    
                            
                    M= float ( math.sqrt(M2) )

                    

                    if math.sqrt(M2) != M:
                        M = math.sqrt(M2)

                    if math.sqrt(M2) == M:
                        Q=1
                    else: 
                        Q= abs(M-math.sqrt(M2))
            
                VARIABLE_M_2 = str(  float (M2)  )
                VARIABLE_M_3 = str( float (Le1)  )
                VARIABLE_M_4 = str( float (Le2)  )
                VARIABLE_M_5 = str( float (math.sqrt(M2))  )
        
     
            
    

    #Se cambia texto de label, con ayuda de "condigure()"
    #Ver forma de obtener info de Entry asociado al nombre...
    #...es a traves de la variable "nombre_usuario", llamando a "get()"
    

    label_resultadoM2.configure( text = "{}".format( VARIABLE_M_2) )
    label_resultadoLE1.configure( text = "{}".format(VARIABLE_M_3) )
    label_resultadoLE2.configure( text = "{}".format(VARIABLE_M_4) )
    label_resultadoM1.configure( text = "{}".format(VARIABLE_M_5) )

b_1 = ttk.Button( root, text = "PROCESAR VALORES" , command = funcion_tocame)
b_1.grid(row =6, column = 0, padx = (10,10))
#Mirar padx como "padding en x externo"


#Se crea automaticamente la ventana con todas las especificaciones aqui.
#NOTA: aqui se queda el codigo de Python corriendo indefinidamente (hasta salir de ventana)
root.mainloop()
