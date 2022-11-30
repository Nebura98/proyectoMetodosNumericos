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

        f_a = funcion(intervaloMenor, ecuacion)
        f_b = funcion(intervaloMayor, ecuacion)

        puntoMedio =  intervaloMayor - f_b * (intervaloMayor - intervaloMenor) / (f_b - f_a )
  
        error = round(abs((puntoMedio - intervaloMenor) / puntoMedio) * 100, body.decimales)
        
        resultado[repr(indice)] = {
            'intervaloMenor': round(intervaloMenor, decimales),
            'intervaloMayor': round(intervaloMayor, decimales),
            'puntoMedio': round(puntoMedio, decimales),
            'error': str(error) + '%'
        }

        if puntoMedio>intervaloMenor :
            intervaloMenor = puntoMedio

        if puntoMedio>intervaloMayor :
            intervaloMayor= puntoMedio

        indice += 1

    return resultado
