from scipy.optimize import linprog

# Parámetros del problema
# Coeficientes de la función objetivo (queremos maximizar, así que lo ponemos negativo para que linprog minimice)
c = [-0.3, -0.1, -0.5, -0.2]  # Función objetivo negativa porque linprog minimiza

# Restricciones
# La matriz de coeficientes para las restricciones
A_eq = [
    [1, 1, 0, 0],  # x1 + x2 = 1
    [0, 0, 1, 1]   # y1 + y2 = 1
]

# Los lados derechos de las restricciones
b_eq = [1, 1]

# Restricciones de no negatividad (x1, x2, y1, y2 >= 0)
bounds = [(0, 1), (0, 1), (0, 1), (0, 1)]  # Probabilidades entre 0 y 1

# Usamos linprog para resolver el problema de programación lineal
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
print(resultado)
# Obtener las soluciones óptimas para las variables
x1_opt, x2_opt, y1_opt, y2_opt = resultado.x

# Calcular el promedio de bateo óptimo
z_opt = -resultado.fun  # Recordar que hemos minimizado el negativo de la función objetivo

# Mostrar los resultados
print(f"Probabilidad de que Jim lance una bola rápida (x1): {x1_opt:.4f}")
print(f"Probabilidad de que Jim lance una bola curva (x2): {x2_opt:.4f}")
print(f"Probabilidad de que Joe prediga correctamente una bola rápida (y1): {y1_opt:.4f}")
print(f"Probabilidad de que Joe prediga correctamente una bola curva (y2): {y2_opt:.4f}")
print(f"Promedio de bateo óptimo de Joe: {z_opt:.4f}")
