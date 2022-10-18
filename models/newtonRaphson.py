from pydantic import BaseModel

class NewtonRaphson(BaseModel):
    decimales             : int
    derivadaNewtonRaphson : str
    funcionNewtonRaphson  : str
    tolerancia            : float
    valorInicial          : float


