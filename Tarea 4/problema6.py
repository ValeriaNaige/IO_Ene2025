import numpy as np
from scipy.optimize import linprog

# matriz de acciones por ronda
# A1/A2, A5, B1/B2, B5, C3/C4
A_ub = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

def funcion_objetivo(array):
    sum = 0
    for subarray in array:
        if subarray[-1] == 1:
            sum += 25
        else:
            sum += 20
    
    return sum

res = funcion_objetivo(A_ub)

print("El tiempo total es: ", res)