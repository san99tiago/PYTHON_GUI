#Santiago Garcia Arango, 16 Enero 2020
#SE APRENDE A TRABAJAR CON FRAMES (con pack() )
#------------------------------------------------------------------------

#Los Frames son una especie de "contenedores" que facilitaran la organizacion visual...
#... el objetivo es que se organice visualmente el programa con ayuda de Frames que a su vez...
#... se disponen en la ventana principal de trabajo (que la hemos llamado root)
#Es decir:
#Permite crear Frames dentro del root, para organizacion mas sencilla, algo asi:
# ROOT:
# **************************************************************
# *                                                            *    
# *                                                            *    
# *                        FRAME 1                             *    
# *                                                            *    
# *                                                            *    
# *                                                            *    
# *                                                            *    
# **************************************************************
# *                            *                               *    
# *                            *                               *    
# *                            *                               *    
# *                            *                               *    
# *        FRAME 2             *             FRAME 3           *    
# *                            *                               *    
# *                            *                               *    
# *                            *                               *    
# *                            *                               *    
# *                            *                               *    
# **************************************************************


#------------------------------------------------------------------------


#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("FRAMES")

#IMPORTANTE: observar que cada Frame se agrega al root
#Se crea el Frame 1 (contenedor 1 de la ventana), indicando el parent (root)
Frame_1 = ttk.Frame(root)
Frame_1.pack(side = "top", fill = "both", expand = True)

#Se crea el Frame 2 (contenedor 2 de la ventana), indicando el parent (root)
Frame_2 = ttk.Frame(root)
Frame_2.pack(side = "left", fill = "both", expand = True)

#Se crea el Frame 3 (contenedor 3 de la ventana), indicando el parent (root)
Frame_3 = ttk.Frame(root)
Frame_3.pack(side = "left", fill = "both", expand = True)

#Se agregan widets al Frame_1
L1 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "white" )
L1.pack(side = "top",expand = True, fill = "both")
L2 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "yellow" )
L2.pack(side = "top",expand = True, fill = "both")
L3 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "red" )
L3.pack(side = "top",expand = True, fill = "both")

#Se agregan widets al Frame_2
L4 = tk.Label( Frame_2, text = "TEXTO EN FRAME 2", bg = "white",fg = "black" )
L4.pack(side = "top",expand = True, fill = "both")
L5 = tk.Label( Frame_2, text = "TEXTO EN FRAME 2", bg = "white",fg = "blue" )
L5.pack(side = "top",expand = True, fill = "both")

#Se agregan widets al Frame_3
L6 = tk.Label( Frame_3, text = "TEXTO EN FRAME 3", bg = "yellow",fg = "black" )
L6.pack(side = "top",expand = True, fill = "both")
L7 = tk.Label( Frame_3, text = "TEXTO EN FRAME 3", bg = "yellow",fg = "green" )
L7.pack(side = "top",expand = True, fill = "both")

#Se ejecuta el "mainloop" que permite correr el codigo de la ventana correctamente
root.mainloop()
