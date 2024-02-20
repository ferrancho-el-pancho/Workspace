from tkinter import *

#Crea la ventana principal 
ventana = Tk()
ventana.title('Mi aplicación')

#Creación de un marco
marco1 = Frame(ventana, height=200, width=100, bg='green')
marco1.grid(row=0, column=0)

#Bucle evento principal 
ventana.mainloop()