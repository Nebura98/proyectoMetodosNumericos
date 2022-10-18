from pydantic import BaseModel

class Secante(BaseModel):
    ecuacion       : str
    intervaloMenor : float    
    intervaloMayor : float
    tolerancia     : float