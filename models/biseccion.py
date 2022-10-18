from pydantic import BaseModel

class Biseccion(BaseModel):
    ecuacion       : str
    intervaloMenor : float    
    intervaloMayor : float
    tolerancia     : float