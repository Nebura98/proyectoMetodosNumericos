from pydantic import BaseModel

class Secante(BaseModel):
    decimales      : int
    ecuacion       : str
    intervaloMayor : float
    intervaloMenor : float    
    tolerancia     : float