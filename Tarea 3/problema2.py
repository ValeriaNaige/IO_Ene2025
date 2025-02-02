import scipy.optimize as opt

# Función objetivo: maximizar el área, que es w*h
# En realidad, minimizamos el negativo del área para maximizarlo
def objetivo(x):
    w, h = x
    return -(w * h)

# Restricciones
def restriccion(x, L):
    w, h = x
    return 2 * (w + h) - L  # 2(w + h) = L

# Función para resolver el problema
def resolver_problema(L):
    # Condiciones iniciales (aproximación inicial de w y h)
    x0 = [L / 4, L / 4]  # Valor inicial, sugiere que w = h inicialmente
    
    # Definir las restricciones
    restricciones = ({'type': 'eq', 'fun': restriccion, 'args': (L,)})
    
    # Definir los límites para w y h (no pueden ser negativos)
    limites = [(0, None), (0, None)]  # w ≥ 0, h ≥ 0
    
    # Usar el optimizador de scipy para maximizar el área
    resultado = opt.minimize(objetivo, x0, constraints=restricciones, bounds=limites)
    
    # Si la optimización fue exitosa
    if resultado.success:
        w_optimo, h_optimo = resultado.x
        area_optima = -resultado.fun  # Recuperar el valor máximo del área
        return w_optimo, h_optimo, area_optima
    else:
        raise ValueError("No se pudo encontrar una solución óptima.")

# Pedir la longitud del alambre al usuario
L = float(input("Introduce la longitud del alambre (en pulgadas): "))

# Resolver el problema
w_optimo, h_optimo, area_optima = resolver_problema(L)

# Mostrar el resultado
print(f"El ancho óptimo es: {w_optimo:.2f} pulgadas")
print(f"La altura óptima es: {h_optimo:.2f} pulgadas")
print(f"El área máxima del rectángulo es: {area_optima:.2f} pulgadas cuadradas")
