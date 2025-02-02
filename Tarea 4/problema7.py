import pulp

# Definición de los puntos iniciales en cada capa
C1 = {1, 2, 3, 4}  # Puntos iniciales en la capa 1
C2 = {5, 6, 7}     # Puntos iniciales en la capa 2
C3 = {8, 9}        # Puntos iniciales en la capa 3
C4 = {10}           # Punto inicial en la capa 4

# Definición de los puntos existentes y las capas
i = list(C1 | C2 | C3 | C4)  # Todos los puntos
j_values = [1, 2, 3, 4]      # Las capas

# Definición de variables binarias x_ij: Si el punto i está en la capa j
x = pulp.LpVariable.dicts('x', (i, j_values), cat='Binary')

# Definición de variables binarias y_ij: Si el punto i se movió a la capa j
y = pulp.LpVariable.dicts('y', (i, j_values), cat='Binary')

# Problema de optimización
prob = pulp.LpProblem("Invertir_piramide", pulp.LpMinimize)

# Función objetivo: minimizar la cantidad de movimientos
prob += pulp.lpSum([y[i][j] for i in i for j in j_values]), "Minimizar_movimientos"

# Restricción 1: Cada punto debe estar exactamente en una capa
for point in i:
    prob += pulp.lpSum([x[point][layer] for layer in j_values]) == 1, f"Restriccion_ubicacion_{point}"

# Restricción 2: Cada capa debe tener un número definido de puntos al final
prob += pulp.lpSum([x[point][1] for point in i]) == 1, "Restriccion_capa_1"
prob += pulp.lpSum([x[point][2] for point in i]) == 2, "Restriccion_capa_2"
prob += pulp.lpSum([x[point][3] for point in i]) == 3, "Restriccion_capa_3"
prob += pulp.lpSum([x[point][4] for point in i]) == 4, "Restriccion_capa_4"


# Restricciones adicionales de movimientos:
# La capa 4 debe llenarse con 3 puntos de la capa 1 (sin aceptar puntos de otras capas)
prob += pulp.lpSum([y[point][4] for point in C1]) == 3, "Restriccion_movimiento_capa_4"

# La capa 3 debe llenarse con 1 punto de la capa 2 (sin aceptar puntos de otras capas)
prob += pulp.lpSum([y[point][3] for point in C2]) == 1, "Restriccion_movimiento_capa_3"

# Restricciones de que las capas 1 y 2 no deben aceptar nuevos puntos
prob += pulp.lpSum([y[point][1] for point in i]) == 0, "Restriccion_movimiento_capa_1"
prob += pulp.lpSum([y[point][2] for point in i]) == 0, "Restriccion_movimiento_capa_2"

# Resolver el problema
prob.solve()

# Imprimir el resultado
if pulp.LpStatus[prob.status] == 'Optimal':
    print("Solución óptima encontrada:")
    total_movimientos = sum(pulp.value(y[i][j]) for i in i for j in j_values)
    print(f"Total de movimientos realizados: {total_movimientos}")
    

    for point in i:
        for layer in j_values:
            if pulp.value(y[point][layer]) ==1:
                print(f"Punto {point} se movió a la capa {layer}")
else:
    print("No se encontró solución óptima.")
