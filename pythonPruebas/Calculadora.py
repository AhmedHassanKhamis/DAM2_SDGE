'''
Created on 21 oct 2024

@author: usertar
'''
import tkinter as tk 
from tkinter import ttk 
from Calculos import Calculos

# PARTE DE LA CREACION DE LA VENTANA
interruptor = False
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(1, 1)

# RESULTADO
resultadoVista = ttk.Label(ventana, text="")
resultadoVista.grid(column=3, row=0)


# PARTE DE LOS BOTONES
numeros = ""
numeros2 = ""
operador = ""
botones = [["AC","^","*","!"],
               ["7","8","9","/"],
               ["4","5","6","+"],
               ["1","2","3","-"],
               ["0",".","%","="]]


# EJEMPLO BOTON
# btn = ttk.Button(ventana, text="AC", command= limpiar)
# btn.grid(column=0, row=1)

# FUNCIONES

def limpiarNumeros():
     global numeros, numeros2, operador
     numeros = ""
     numeros2 = ""
     operador = ""

def limpiar():
     global resultadoVista, numeros, numeros2, operador
     resultadoVista['text'] = ""
     numeros = ""
     numeros2 = ""
     operador = ""



def guardarOperacion(evento):
     global resultadoVista, numeros, numeros2, operador
     boton = evento.widget.cget("text")
     if boton != "AC":
          resultadoVista['text'] = str(resultadoVista['text']) + boton
     if boton == "AC":
          limpiar()
     elif boton in ["+","-","*","/","%","!","^"]:
          operador = boton
     elif boton == "." and operador == "":
          numeros += "."
     elif boton == "." and operador != "":
          numeros2 += "."
     elif boton == "=":
          print(numeros)
          print(numeros2)
          resultadoVista['text'] = ""
          calcular()
          limpiarNumeros()
     elif boton in ["0","1","2","3","4","5","6","7","8","9"] and operador == "":
          numeros += boton
     elif boton in ["0","1","2","3","4","5","6","7","8","9"] and operador != "":
          numeros2 += boton


def calcular():
     if operador == "+":
          resultadoVista['text'] = Calculos.sumar(float(numeros),float(numeros2))
          limpiarNumeros()
     elif operador == "-":
          resultadoVista['text'] = Calculos.restar(float(numeros),float(numeros2))
          limpiarNumeros()
     elif operador == "*":
          resultadoVista['text'] = Calculos.multiplicar(float(numeros),float(numeros2))
          limpiarNumeros()
     elif operador == "/":
          resultadoVista['text'] = Calculos.dividir(float(numeros),float(numeros2))
          limpiarNumeros()
     elif operador == "%":
          resultadoVista['text'] = Calculos.modulo(float(numeros),float(numeros2))
          limpiarNumeros()
     elif operador == "!":
          resultadoVista['text'] = Calculos.factorial(float(numeros))
          limpiarNumeros()
     elif operador == "^":
          resultadoVista['text'] = Calculos.potencia(float(numeros),float(numeros2))
          limpiarNumeros()



# Diccionario para mantener referencias de los botones
diccionarioBotones = {}
# Número de filas que contienen botones
for i in range(len(botones)):  
     # Número de columnas  
     for j in range(len(botones[i])):  
          # Creando los botones
          diccionarioBotones["btn_"+str(botones[i][j])] = ttk.Button(ventana, text=str(botones[i][j]))
           
          # Posicionando los botones
          diccionarioBotones["btn_"+str(botones[i][j])].grid(row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
           
          # Asignando una acción a los botones
          diccionarioBotones["btn_"+str(botones[i][j])].bind('<Button-1>', guardarOperacion)


ventana.mainloop()

