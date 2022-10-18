import re
import math

from helpers.remplazarSimbolos import remplazarSimbolos

def funcion(x, ecuacion):
    return eval(re.sub('^x$',str(x),ecuacion))

def procesoNewtonRaphson(valores):
    indice = 0  
    xn = valores.valorInicial
    error = 100
    
    funcionNewtonRaphson = remplazarSimbolos(valores.funcionNewtonRaphson)
    derivadaNewtonRaphson = remplazarSimbolos(valores.derivadaNewtonRaphson)

    resultado = {}

    while  error > valores.tolerancia:
        try:
            indice = indice + 1
            xi = round(xn-funcion(xn, funcionNewtonRaphson)/funcion(xn, derivadaNewtonRaphson), 4)
            error = round(abs((xi-xn)/xi)*100, 4)
            resultado[repr(indice)] = repr('x = ' + str(xi) + ', Punto medio = ' + str(funcion(xi)) + ', Error: ' + str(error) + '%')
            xn = xi
        except OverflowError as err:
            print ('Overflowed on power ', xi, err)
            break
    return resultado