import pulp

# Número de variables (R_1, R_2, ..., R_10)
n = 10

# Crear un problema de minimización
prob = pulp.LpProblem("Minimizar_Recompensas", pulp.LpMinimize)

# Crear variables R_i, que son enteras y mayores que 0
R = [pulp.LpVariable(f"Recompensa_multiplo_{i+1}", lowBound=1, cat='Integer') for i in range(n)]  # Variables enteras y >= 1

# Función objetivo: Minimizar la suma de R_i
prob += pulp.lpSum(R), "Suma_Recompensas"

# Resolver el problema
prob.solve()

# Mostrar los resultados
if pulp.LpStatus[prob.status] == "Optimal":
    print("La solución óptima encontrada es\n")
    for r in R:
        print(f"{r}: {r.varValue}")

    print("\n\nLa suma mínima será de:", pulp.value(prob.objective))
else:
    print("No se pudo encontrar una solución óptima")