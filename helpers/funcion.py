import re
import math

def funcion(x, ecuacion):
    try:
        return eval(re.sub('^x$',str(x),ecuacion))
    except:
        print('Heloooooooooo')
