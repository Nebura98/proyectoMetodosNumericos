from pydantic import BaseModel

class PuntoFijo(BaseModel):
    ecuacion     : str
    valorInicial : float
    tolerancia   : float
