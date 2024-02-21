from tkinter import *

operador = ''
numero1 = 0

def operacion (op):
    global numero1
    global operador
    numero1= float (textbox.get())
    operador = op
    textbox.delete(0, END)

def add():
    operacion('+')

def minus():
    operacion('-')

def times():
    operacion('*')

def divide():
    operacion('/')

def clear():
    textbox.delete(0, END)

def evaluate():
    numero2= float(textbox.get())

    textbox.delete(0, END)


    if operador == '+':
        textbox.insert (END, numero1 + numero2)
    
    elif operador == '-':
        textbox.insert (END, numero2 - numero2)

    elif operador =='*':
        textbox.insert (END, numero1 * numero2)

    elif operador == '/':
        textbox.insert (END, numero1 / numero2)

    else: 
        textbox.insert (END, 'Error')



#Crea la ventana principal 
ventana = Tk()
ventana.title('Calculadora')

textbox = Entry(ventana, width=20)
textbox.grid ( row=0, column=0, columnspan=3)

boton_suma = Button(ventana, text='+', width=3, command=add)
boton_suma.grid (row=2, column=0)

boton_resta = Button(ventana, text='-', width=3, command=minus)
boton_resta.grid (row=2, column=1)

boton_multiplicar = Button(ventana, text='*', width=3, command=times)
boton_multiplicar.grid (row=3, column=0)

boton_dividir = Button(ventana, text='/', width=3, command=divide)
boton_dividir.grid (row=3, column=1)

boton_igual = Button(ventana, text='=', width=6, command=evaluate)
boton_igual.grid (row=4, column=0, columnspan=2)

boton_limpiar = Button(ventana, text='CLEAR', width=6, command=clear)
boton_limpiar.grid (row=4, column=2, sticky=E)

#Bucle evento principal 
ventana.mainloop()