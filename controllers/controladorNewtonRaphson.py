from helpers.funcion import funcion
from helpers.remplazarSimbolos import remplazarSimbolos

from models.newtonRaphson import NewtonRaphson


def procesoNewtonRaphson(body: NewtonRaphson):
    indice = 1
    xn = body.valorInicial
    xiAnterior = 0
    error = 100

    funcionNewtonRaphson = remplazarSimbolos(body.funcionNewtonRaphson)
    derivadaNewtonRaphson = remplazarSimbolos(body.derivadaNewtonRaphson)

    resultado = {}

    while error > body.tolerancia:
        try:

            f_a = funcion(xn, funcionNewtonRaphson) 
            f_b= funcion(xn, derivadaNewtonRaphson)

            xi = xn - (f_a / f_b)
            
            error = round(abs((xi - xiAnterior) / xi) * 100, body.decimales)

            xiAnterior=xi
            
            resultado[repr(indice)] = {
                'x': str(round(xn, body.decimales)),
                'puntoMedio': (round(f_a, body.decimales)),
                'error': str(error) + '%'
            }
            xn = xi
            indice += 1
        except OverflowError as err:
            print('Overflowed on power ', xi, err)
            break
    return resultado
