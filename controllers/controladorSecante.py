import math
import re

from helpers.remplazarSimbolos import remplazarSimbolos

def funcion(x, ecuacion):
    return eval(re.sub('^x$',str(x),ecuacion))

def procesoSecante(body):
    ecuacion, intervaloMenor, intervaloMayor, tolerancia = body
    ecuacion =  remplazarSimbolos(ecuacion)
    indice = 1
    error = 100
    while error > tolerancia:
        if funcion(intervaloMenor, ecuacion) == funcion(intervaloMayor, ecuacion):
            print('Divide by zero error!')
            break
        x2 = intervaloMenor - (intervaloMayor-intervaloMenor)*funcion(intervaloMenor, ecuacion)/( funcion(intervaloMayor,ecuacion) - funcion(intervaloMenor,ecuacion) ) 
        print('Iteration-%d, x2 = %0.6f and funcion(x2) = %0.6f' % (indice, x2, funcion(x2)))
        intervaloMenor = intervaloMayor
        intervaloMayor = x2
        indice = indice + 1

        condition = abs(funcion(x2)) > tolerancia
        condition