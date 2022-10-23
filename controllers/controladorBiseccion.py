from helpers.funcion import funcion
from helpers.remplazarSimbolos import remplazarSimbolos

from models.biseccion import Biseccion


def procesoBiseccion(body: Biseccion):

    ecuacion = remplazarSimbolos(body.ecuacion)
    intervaloMenor = body.intervaloMenor
    intervaloMayor = body.intervaloMayor
    decimales = body.decimales
    tolerancia = body.tolerancia
    
    indice = 1
    error = 100

    f_c = 0
    puntoMedioAnterior = 0

    resultado = {}

    while error > tolerancia:

        puntoMedio = (intervaloMenor + intervaloMayor) / 2

        error = abs((puntoMedio - puntoMedioAnterior) / puntoMedio) * 100

        puntoMedioAnterior = puntoMedio

        f_a = funcion(intervaloMenor, ecuacion)
        f_b = funcion(intervaloMayor, ecuacion)
        f_c = funcion(puntoMedio, ecuacion)

        if (f_a * f_c) < 0:
            intervaloMayor = puntoMedio

        if (f_b * f_c) < 0:
            intervaloMenor = puntoMedio

        resultado[repr(indice)] = {
            'intervaloMenor': round(intervaloMenor, decimales),
            'intervaloMayor': round(intervaloMayor, decimales),
            'raiz': round(puntoMedio, decimales),
            'error': str(round(error, decimales)) + '%'
        }

        indice += 1

    return resultado
