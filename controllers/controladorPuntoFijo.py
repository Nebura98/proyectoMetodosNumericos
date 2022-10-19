from helpers.funcion import funcion
from helpers.remplazarSimbolos import remplazarSimbolos

from models.puntoFijo import PuntoFijo

def procesoPuntoFijo(body:PuntoFijo):

    ecuacion = remplazarSimbolos(body.ecuacion)
    
    xi = body.valorInicial
    
    error = 100
    indice = 1
    
    resultado = {}
    
    while (error > body.tolerancia):
        xn = funcion(xi, ecuacion)
        error = abs((xn - xi) / xn) * 100
        xi = xn
        resultado[repr(indice)] = {
            'x': str(round(xn, body.decimales)),
            'error': str(round(xn, body.decimales)) + '%'
        }
        indice += 1
    return resultado
