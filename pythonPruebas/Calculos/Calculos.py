'''
Created on 21 oct 2024

@author: usertar
'''
def sumar(v1,v2):
    return v1 + v2

def restar(v1,v2):
    return v1 - v2

def dividir(v1,v2):
    return v1 / v2

def multiplicar(v1,v2):
    return v1 * v2

def modulo(v1,v2):
    return v1 % v2

def factorial(v1):
    if v1 == 0:
        return 1
    else:
        return v1 * factorial(v1 - 1)

def potencia(v1,v2):
    return v1 ** v2