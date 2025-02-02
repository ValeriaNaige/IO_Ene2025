import pulp

# Parámetros del problema
n = 4  # Número de cadenas
m = 3  # Número de eslabones por cadena
coste_romper = 2  # Costo de romper un eslabón (en centavos)
coste_soldar = 3  # Costo de soldar un eslabón (en centavos)

# Crear el problema de optimización
prob = pulp.LpProblem("Minimizar_costo_conexion", pulp.LpMinimize)

# Variables de decisión: x(i, j) indica si el eslabón j de la cadena i se rompe (y se vuelve a soldar)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(1, n + 1) for j in range(1, m + 1)), cat='Binary')

# Función objetivo: Minimizar el costo total (romper + soldar eslabones)
# El costo total será 5 centavos por cada eslabón que se rompa y se solda.
prob += pulp.lpSum(5 * x[(i, 3)] for i in range(1, n + 1)), "Costo_Total"

# Restricción 1: Solo se puede romper el eslabón 3 de cada cadena
for i in range(1, n + 1):
    prob += x[(i, 3)] == 1, f"Romper_eslabon_3_cadena_{i}"

# Restricción 2: El eslabón 1 de la cadena i debe conectarse al eslabón 3 de la cadena i-1 (circular)
for i in range(2, n + 1):
    prob += x[(i - 1, 3)] == x[(i, 1)], f"Conectar_eslabon_1_cadena_{i}_a_eslabon_3_cadena_{i-1}"

# Restricción 3: El eslabón 1 de la primera cadena se conecta al eslabón 3 de la última cadena
prob += x[(n, 3)] == x[(1, 1)], "Conectar_eslabon_3_cadena_n_a_eslabon_1_cadena_1"

# Resolver el problema
prob.solve()

# Mostrar la solución
if pulp.LpStatus[prob.status] == 'Optimal':
    print(f"Costo total del brazalete: {pulp.value(prob.objective)} centavos")

    # Imprimir qué eslabón se está rompiendo y soldando (solo eslabón 3 se rompe)
    for i in range(1, n + 1):
        if pulp.value(x[(i, 3)]) == 1:
            print(f"Se rompe el eslabón 3 de la cadena {i} y se solda a la siguiente cadena.")

    # Identificar el eslabón conectado entre cada par de cadenas (conexión circular)
    for i in range(1, n + 1):
        siguiente = i % n + 1  # La siguiente cadena (circular)
        if pulp.value(x[(i, 3)]) == 1:  # Solo mostrar conexiones si se rompe el eslabón 3
            if i==1:
                print(f"El eslabón 1 de la cadena {i} se conecta al eslabón 3 de la cadena {i+3}.")
            else:
                print(f"El eslabón 1 de la cadena {i} se conecta al eslabón 3 de la cadena {i-1}.")
else:
    print("No se encontró una solución óptima.")
