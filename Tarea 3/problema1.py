import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo (costos de los boletos)
c = [400, 320, 400, 320, 300, 300]  # Coeficientes correspondientes a FDF, FDF_S, DFD, DFD_S, FD, DF

# Matriz de restricciones (igualdades transformadas en desigualdades)
A_ub = [
    [-1, -1, 0, 0, -1, 0],  # FDF + FDF_S + FD >= 1
    [-2, -2, -2, -2, -1, -1],  # 2*(FDF + FDF_S + DFD + DFD_S) + FD + DF >= 10
    [-1, -1, -1, -1, -1, 0],  # FDF + FDF_S + FD + DFD + DFD_S >= 5 (vuelos de ida)
    [-1, -1, -1, -1, 0, -1],  # DFD + DFD_S + DF + FDF + FDF_S >= 5 (vuelos de regreso)
    [0, 0, 0, 0, -1, -1], # FD = DF (relación entre vuelos sencillos de ida y vuelta)
]

# Lado derecho de las restricciones
b_ub = [-1, -10, -5, -5, 0]  # Los valores de las restricciones (negativos para convertir a <=)

# Matriz de restricciones de no negatividad
bounds = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None)]  # No negatividad

# Resolver el problema de programación lineal
resultado = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Verificar si la optimización fue exitosa
if resultado.success:
    # Obtener los resultados
    FDF, FDF_S, DFD, DFD_S, FD, DF = np.round(resultado.x).astype(int)

    # Imprimir los resultados
    print(f"FDF (Viaje redondo de Fayetteville a Denver entre semana): {FDF}")
    print(f"FDF_S (Viaje redondo de Fayetteville a Denver con fin de semana): {FDF_S}")
    print(f"DFD (Viaje redondo de Denver a Fayetteville entre semana): {DFD}")
    print(f"DFD_S (Viaje redondo de Denver a Fayetteville con fin de semana): {DFD_S}")
    print(f"FD (Viaje directo de Fayetteville a Denver): {FD}")
    print(f"DF (Viaje directo de Denver a Fayetteville): {DF}")
    print(f"Costo total: {resultado.fun:.2f}")
else:
    # Si la optimización no fue exitosa, imprimir el mensaje de error
    print("La optimización no se pudo resolver.")
    print(f"Mensaje de error: {resultado.message}")
