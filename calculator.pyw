'''

Calculator:
1.- With 2 entry
2.- With 4 buttons to execute the basics math operations.
3.- display the result to the user via an alert
 
'''

from tkinter import *
from tkinter import messagebox as ALERTA

#Window:
root = Tk()
root.geometry("200x250")
root.title("Calculator")
root.iconbitmap("img/icono_calculadora.ico")
root.config(bg="Green")
root.resizable(False,False)

#Variables:
num1 = StringVar()
num2 = StringVar()
result = StringVar()

#Functions:
def addition():
    try:
        result.set(float(num1.get()) + float(num2.get()))
        showResuts()
    except:
        ALERTA.showerror("ERROR!","ERROR! Type just numbers. Try again...")


def subtraction():
    try:
        result.set(float(num1.get()) - float(num2.get()))
        showResuts()
    except:
        ALERTA.showerror("ERROR!","ERROR! Type just numbers. Try again...")


def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
        showResuts()
    except:
        ALERTA.showerror("ERROR!","ERROR! Type just numbers. Try again...")


def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
        showResuts()
    except:
        ALERTA.showerror("ERROR!","ERROR! Type just numbers. Try again...")


def showResuts():
    ALERTA.showinfo("result", f"The result is: {result.get()} ")

def salirPrograma():
    result = ALERTA.askquestion("Exit", "¿Are you sure to Exit?")

    if result != 'no':
        ALERTA.showinfo("", "Bye :(")
        root.destroy()



#Entrys:
title = Label(root, text="Type the first number:", font=("Comic Sans MS", 11))
title.grid(row=0, column=0, columnspan= 5, sticky=N)
entry1 = Entry(root, textvariable=num1)
entry1.config(width=27)
entry1.grid(row=1, column=0, pady=12, sticky=NW, columnspan= 5)

title = Label(root, text="Type the second number:", font=("Comic Sans MS", 11))
title.grid(row=2, column=0, columnspan= 5, sticky=N)
entry2 = Entry(root, textvariable=num2)
entry2.config(width=27)
entry2.grid(row=3, column=0, pady=12, sticky=NW, columnspan= 5)



#Buttons:
buttonAdd = Button(root, text="+", padx=7, pady=5, command=lambda:addition())
buttonAdd.grid(row=4,column=0, columnspan= 5, sticky=W, padx=12)

buttonSubstact = Button(root, text="-", padx=7, pady=5, command=lambda:subtraction())
buttonSubstact.grid(row=4,column=1, columnspan= 5, sticky=W, padx=12)

buttonMult = Button(root, text="x", padx=7, pady=5, command=lambda:multiply())
buttonMult.grid(row=4,column=2, columnspan= 5, sticky=W, padx=12)

buttonDiv = Button(root, text="/", padx=7, pady=5, command=lambda:divide())
buttonDiv.grid(row=4,column=3, columnspan= 5, sticky=W, padx=12)


buttonExit = Button(root, text="Exit", command=lambda: salirPrograma())
buttonExit.config(
    bg="blue",
    fg="white",
    font=("Comic Sans MS", 10),
)
buttonExit.grid(row=4, column=4)



root.mainloop()