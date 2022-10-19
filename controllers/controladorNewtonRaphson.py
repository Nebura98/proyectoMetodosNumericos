from helpers.funcion import funcion
from helpers.remplazarSimbolos import remplazarSimbolos

from models.newtonRaphson import NewtonRaphson


def procesoNewtonRaphson(body: NewtonRaphson):
    indice = 1
    xn = body.valorInicial
    error = 100

    funcionNewtonRaphson = remplazarSimbolos(body.funcionNewtonRaphson)
    derivadaNewtonRaphson = remplazarSimbolos(body.derivadaNewtonRaphson)

    resultado = {}

    while error > body.tolerancia:
        try:
            xi = xn - funcion(xn, funcionNewtonRaphson) / \
                funcion(xn, derivadaNewtonRaphson)
            error = round(abs((xi - xn) / xi) * 100, body.decimales)

            resultado[repr(indice)] = {
                'x': str(round(xi, body.decimales)),
                'puntoMedio': (round(funcion(xi, funcionNewtonRaphson), body.decimales)),
                'error': str(error) + '%'
            }
            xn = xi
            indice += 1
        except OverflowError as err:
            print('Overflowed on power ', xi, err)
            break
    return resultado
