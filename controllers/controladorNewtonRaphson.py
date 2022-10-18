from helpers.funcion import funcion
from helpers.remplazarSimbolos import remplazarSimbolos

from models.newtonRaphson import NewtonRaphson

def procesoNewtonRaphson(body : NewtonRaphson):
    indice = 0  
    xn     = body.valorInicial 
    error  = 100
    
    funcionNewtonRaphson  = remplazarSimbolos(body.funcionNewtonRaphson)
    derivadaNewtonRaphson = remplazarSimbolos(body.derivadaNewtonRaphson)

    resultado = {}

    while  error > body.tolerancia:
        try:
            indice = indice + 1
            xi = xn - funcion(xn, funcionNewtonRaphson) / funcion(xn, derivadaNewtonRaphson)
            error = round(abs((xi-xn)/xi)*100,body.decimales)

            resultado[repr(indice)] = {
                'X' : str(round(xi,body.decimales)),
                'Punto medio' : (round(funcion(xi,funcionNewtonRaphson),body.decimales)),
                'Error':  str(error) + '%'
            }

            xn = xi
        except OverflowError as err:
            print ('Overflowed on power ', xi, err)
            break
    return resultado