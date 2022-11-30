from fastapi import HTTPException
import re
import math
math.pi

def funcion(x, ecuacion):
    try:
        return eval(re.sub('^x$',str(x),ecuacion))
    except:
        raise HTTPException(status_code=500, detail="La funcion ha sido ingresada erróneamente, por favor revise los datos.")
