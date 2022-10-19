from fastapi import FastAPI
from controllers.controladorBiseccion import procesoBiseccion
from controllers.controladorPuntoFijo import procesoPuntoFijo

# Clases
from models.biseccion import Biseccion
from models.newtonRaphson import NewtonRaphson
from models.puntoFijo import PuntoFijo
from models.secante import Secante

# Controladores
from controllers.controladorNewtonRaphson import procesoNewtonRaphson
from controllers.controladorSecante import procesoSecante

app = FastAPI()


@app.get('/biseccion')
def Biseccion(body: Biseccion):
    resultado = procesoBiseccion(body)
    return resultado


@app.get('/newton-raphson')
def newtonRaphson(body: NewtonRaphson):
    resultado = procesoNewtonRaphson(body)
    return resultado


@app.get('/punto-fijo')
def puntoFijo(body: PuntoFijo):
    resultado = procesoPuntoFijo(body)
    return resultado


@app.get('/secante')
def secante(body: Secante):
    resultado = procesoSecante(body)
    return resultado