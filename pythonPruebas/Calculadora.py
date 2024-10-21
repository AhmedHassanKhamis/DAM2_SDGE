'''
Created on 21 oct 2024

@author: usertar
'''
import tkinter as tk 
from tkinter import ttk 
from Calculos import Calculos

interruptor = False
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(1, 1)
resultado =ttk.Label(ventana, text="0")
resultado.grid(column=3, row=0)
operador = ""
numeros = [0,1,2,3,4,5,6,7,8,9]
operadores  = ["/","*","-","+","%","!"]

# def funcionPrueba():
#         global interruptor
#         if interruptor==True:
#             btn.configure(text="a")
#         else:
#             btn.configure(text="Pulsa")
#         interruptor=not interruptor
        
def guardarOperador():
     operador = btn['text']
        
def guardarValor():
     numeros.append(btn["text"])

def calcular():
     if operador == "+":
          resultado['text'] = Calculos.sumar(numeros[0],numeros[1])
          numeros = []
     elif operador == "-":
          resultado['text'] = Calculos.restar(numeros[0],numeros[1])
          numeros = []
     elif operador == "*":
          resultado['text'] = Calculos.multiplicar(numeros[0],numeros[1])
          numeros = []
     elif operador == "/":
          resultado['text'] = Calculos.dividir(numeros[0],numeros[1])
          numeros = []
     elif operador == "%":
          resultado['text'] = Calculos.modulo(numeros[0],numeros[1])
          numeros = []
     elif operador == "x!":
          resultado['text'] = Calculos.factorial(numeros[0],numeros[1])
          numeros = []


def limpiar():
     resultado['text'] = 0
     numeros = []
     operador = ""

a = {}
k = 0
while k < 10:
    # dynamically create key
    key = ...
    # calculate value
    value = ...
    a[key] = value 
    k += 1
     

# segunda fila
btn = ttk.Button(ventana, text="AC", command= limpiar)
btn.grid(column=0, row=1)
btn = ttk.Button(ventana, text="/", command= guardarOperador)
btn.grid(column=1, row=1)
btn = ttk.Button(ventana, text="*", command= guardarOperador)
btn.grid(column=2, row=1)
btn = ttk.Button(ventana, text="-", command= guardarOperador)
btn.grid(column=3, row=1)
# tercera fila
btn = ttk.Button(ventana, text="7", command= guardarValor)
btn.grid(column=0, row=2)
btn = ttk.Button(ventana, text="8", command= guardarValor)
btn.grid(column=1, row=2)
btn = ttk.Button(ventana, text="9", command= guardarValor)
btn.grid(column=2, row=2)
btn = ttk.Button(ventana, text="+", command= guardarOperador)
btn.grid(column=3, row=2)
# cuarta fila
btn = ttk.Button(ventana, text="4", command= guardarValor)
btn.grid(column=0, row=3)
btn = ttk.Button(ventana, text="5", command= guardarValor)
btn.grid(column=1, row=3)
btn = ttk.Button(ventana, text="6", command= guardarValor)
btn.grid(column=2, row=3)
btn = ttk.Button(ventana, text="%", command= guardarOperador)
btn.grid(column=3, row=3)
# quinta fila
btn = ttk.Button(ventana, text="1", command= guardarValor)
btn.grid(column=0, row=4)
btn = ttk.Button(ventana, text="2", command= guardarValor)
btn.grid(column=1, row=4)
btn = ttk.Button(ventana, text="3", command= guardarValor)
btn.grid(column=2, row=4)
btn = ttk.Button(ventana, text="x!", command= guardarOperador)
btn.grid(column=3, row=4)

btn = ttk.Button(ventana, text="Calcular", command= calcular)
btn.grid(column=0, row=5, columnspan=4)


ventana.mainloop()

