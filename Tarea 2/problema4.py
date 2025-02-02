from scipy.optimize import linprog

# Tiempos
T = {('1', '2'): 2, ('1', '3'): 5, ('1', '4'): 10, ('2', '3'): 5, ('2', '4'): 10, ('3', '4'): 10,}
# Variables de decisión (x_AJ, x_AN, ..., r_A, r_J, r_N, r_K)
num_variables = len(T) + 4  # 6 combinaciones de cruces + 4 regresos
c = [T[('1', '2')], T[('1', '3')], T[('1', '4')],
     T[('2', '3')], T[('2', '4')], T[('3', '4')],
     1, 2, 5, 10]  

# Restricciones de igualdad (viajes y regresos)
#   AJ AN AK JN JK NK RA RJ RN RK
A_eq = [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  
    [1, 1, 1, 0, 0, 0, -1, 0, 0, 0],  
    [1, 0, 0, 1, 1, 0, 0, -1, 0, 0],  
    [0, 1, 0, 1, 0, 1, 0, 0, -1, 0],  
    [0, 0, 1, 0, 1, 1, 0, 0, 0, -1], 
]
b_eq = [3, 2, 1, 1, 1, 1]

# Bounds para las variables (0 <= x_ij <= , 0 <= r_i <= 2)
bounds = [(0, 3)] * len(T) + [(0, 2)] * 4


res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')


if res.success:
    print("Solución encontrada:")
    print("Valores de las variables:", res.x)
    print("Tiempo total mínimo:", res.fun)
else:
    print("No se encontró solución.")