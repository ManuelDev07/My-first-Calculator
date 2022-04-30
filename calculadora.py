'''

Calculadora:
1.- Con 2 campos de texto
2.- Con 4 Botones, c/u para las operaciones de matemática básicas.
3.- Mostrar el resultado mediante una ventana de alerta
 
'''

from tkinter import *
from tkinter import messagebox as ALERTA

#Ventana:
raiz = Tk()
raiz.geometry("200x250")
raiz.title("Calculadora")
raiz.iconbitmap("img/icono_calculadora.ico")
raiz.config(bg="Green")
raiz.resizable(False,False)

#Variables:
num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

#Funciones:
def suma():
    try:
        resultado.set(float(num1.get()) + float(num2.get()))
        mostrarResultados()
    except:
        ALERTA.showerror("ERROR!","ERROR! Ingresa solo números. Intenta de nuevo... 😑")


def resta():
    try:
        resultado.set(float(num1.get()) - float(num2.get()))
        mostrarResultados()
    except:
        ALERTA.showerror("ERROR!","ERROR! Ingresa solo números. Intenta de nuevo... 😑")


def multiplicar():
    try:
        resultado.set(float(num1.get()) * float(num2.get()))
        mostrarResultados()
    except:
        ALERTA.showerror("ERROR!","ERROR! Ingresa solo números. Intenta de nuevo... 😑")


def dividir():
    try:
        resultado.set(float(num1.get()) / float(num2.get()))
        mostrarResultados()
    except:
        ALERTA.showerror("ERROR!","ERROR! Ingresa solo números. Intenta de nuevo... 😑")


def mostrarResultados():
    ALERTA.showinfo("Resultado", f"El resultado es: {resultado.get()} ")

def salirPrograma():
    resultado = ALERTA.askquestion("Salir", "¿Quieres salir?")

    if resultado != 'no':
        ALERTA.showinfo("", "Hasta Pronto :(")
        raiz.destroy()



#Entrys:
titulo = Label(raiz, text="Ingresa el Primero Número:", font=("Comic Sans MS", 11))
titulo.grid(row=0, column=0, columnspan= 5, sticky=N)
campo1 = Entry(raiz, textvariable=num1)
campo1.config(width=27)
campo1.grid(row=1, column=0, pady=12, sticky=NW, columnspan= 5)

titulo = Label(raiz, text="Ingresa el Segundo Número:", font=("Comic Sans MS", 11))
titulo.grid(row=2, column=0, columnspan= 5, sticky=N)
campo2 = Entry(raiz, textvariable=num2)
campo2.config(width=27)
campo2.grid(row=3, column=0, pady=12, sticky=NW, columnspan= 5)



#Buttons:
botonSuma = Button(raiz, text="+", padx=7, pady=5, command=lambda:suma())
botonSuma.grid(row=4,column=0, columnspan= 5, sticky=W, padx=12)

botonResta = Button(raiz, text="-", padx=7, pady=5, command=lambda:resta())
botonResta.grid(row=4,column=1, columnspan= 5, sticky=W, padx=12)

botonMult = Button(raiz, text="x", padx=7, pady=5, command=lambda:multiplicar())
botonMult.grid(row=4,column=2, columnspan= 5, sticky=W, padx=12)

botonDiv = Button(raiz, text="/", padx=7, pady=5, command=lambda:dividir())
botonDiv.grid(row=4,column=3, columnspan= 5, sticky=W, padx=12)


botonExit = Button(raiz, text="Salir", command=lambda: salirPrograma())
botonExit.config(
    bg="blue",
    fg="white",
    font=("Comic Sans MS", 10),
)
botonExit.grid(row=4, column=4)



raiz.mainloop()