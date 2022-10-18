import matplotlib
import numpy as np
from matplotlib import pyplot as plt 

def fun(x):
    g= np.cos(x)
    return g

xi= 0
error = 100
while (error>0.001):
    xn=fun(xi)
    error = abs(xn-xi)/xn
    xi=xn
    print (round(xn,5),'             ', round (error,5) )
  
 