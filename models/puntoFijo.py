from pydantic import BaseModel

class PuntoFijo(BaseModel):
    decimales    : int
    ecuacion     : str
    tolerancia   : float
    valorInicial : float
