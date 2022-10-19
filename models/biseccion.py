from pydantic import BaseModel

class Biseccion(BaseModel):
    decimales      : int
    ecuacion       : str
    intervaloMayor : float
    intervaloMenor : float    
    tolerancia     : float