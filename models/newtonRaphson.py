from pydantic import BaseModel

class NewtonRaphson(BaseModel):
    funcionNewtonRaphson  : str
    derivadaNewtonRaphson : str
    tolerancia            : float
    valorInicial          : float


