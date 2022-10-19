from helpers.remplazarSimbolos import remplazarSimbolos
from helpers.funcion import funcion


from models.secante import Secante


def procesoSecante(body:Secante):
    ecuacion = remplazarSimbolos(body.ecuacion)
    indice = 1
    error = 100
    resultado = {}

    intervaloMenor = body.intervaloMenor
    intervaloMayor = body.intervaloMayor
    decimales      = body.decimales
    tolerancia     = body.tolerancia

    while error > tolerancia:
        # if funcion(intervaloMenor,ecuacion) == funcion(intervaloMayor,ecuacion) :
        #     break

        puntoMedio = intervaloMenor - (intervaloMayor - intervaloMenor) * funcion(intervaloMenor, ecuacion) / (funcion(intervaloMayor, ecuacion) - funcion(intervaloMenor, ecuacion))

        error = round(abs((puntoMedio - intervaloMayor) / puntoMedio) * 100, body.decimales)

        resultado[repr(indice)] = {
            'intervaloMenor': round(intervaloMenor, decimales),
            'intervaloMayor': round(intervaloMayor, decimales),
            'puntoMedio': round(puntoMedio, decimales),
            'error': str(error) + '%'
        }

        intervaloMenor = intervaloMayor
        intervaloMayor = puntoMedio
        indice += 1
    return resultado
