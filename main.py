from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Clases
from models.biseccion import Biseccion
from models.newtonRaphson import NewtonRaphson
from models.puntoFijo import PuntoFijo
from models.secante import Secante

# Controladores
from controllers.controladorNewtonRaphson import procesoNewtonRaphson
from controllers.controladorSecante import procesoSecante
from controllers.controladorBiseccion import procesoBiseccion
from controllers.controladorPuntoFijo import procesoPuntoFijo

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/biseccion')
def Biseccion(body: Biseccion):
    resultado = procesoBiseccion(body)
    return resultado


@app.post('/newton-raphson')
def newtonRaphson(body: NewtonRaphson):
    resultado = procesoNewtonRaphson(body)
    return resultado

 
@app.post('/punto-fijo')
def puntoFijo(body: PuntoFijo):
    resultado = procesoPuntoFijo(body)
    return resultado


@app.post('/secante')
def secante(body: Secante):
    resultado = procesoSecante(body)
    return resultado