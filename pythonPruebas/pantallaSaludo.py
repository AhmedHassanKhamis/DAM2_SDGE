'''
Created on 21 oct 2024

@author: usertar
'''
import tkinter as tk 
from tkinter import ttk 


interruptor = False
ventana = tk.Tk()
ventana.title("Titulo")
ventana.resizable(1, 1)
lbEtiqueta =ttk.Label(ventana, text="Hola Mundo")
lbEtiqueta.grid(column=0, row=0)

def funcionPrueba():
        global interruptor
        if interruptor==True:
            btn.configure(text="a")
        else:
            btn.configure(text="Pulsa")
        interruptor=not interruptor
        lbEtiqueta['text'] = "Hello " + entry.get()
btn = ttk.Button(ventana, text="Pulsa", command= funcionPrueba)
btn.grid(column=0, row=2)
entry = ttk.Entry()
entry.grid(column=0, row=1)


ventana.mainloop()

