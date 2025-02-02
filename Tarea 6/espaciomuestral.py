import subprocess
import sys

# Función para verificar si una librería está instalada
def instalar_libreria(libreria):
    try:
        __import__(libreria)
    except ImportError:
        print(f"La librería {libreria} no está instalada. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", libreria])

# Verificar e instalar las librerías necesarias
librerias = ['numpy', 'pandas', 'matplotlib', 'itertools']

for libreria in librerias:
    instalar_libreria(libreria)



import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Definir los 3 dados de 20 caras (numerados del 1 al 20)
dados = range(1, 21)

# Generar todas las combinaciones posibles de los lanzamientos de los 3 dados
combinaciones = list(itertools.product(dados, repeat=3))

# Sumar los resultados de cada combinación
sumas = [sum(combinacion) for combinacion in combinaciones]

# Calcular las frecuencias de las sumas
frecuencias = {suma: sum(1 for s in sumas if s == suma) for suma in set(sumas)}

# Ordenar las sumas y sus frecuencias
frecuencias_ordenadas = sorted(frecuencias.items())

# Crear un DataFrame para mostrar la tabla de frecuencias
df = pd.DataFrame(frecuencias_ordenadas, columns=["Suma", "Frecuencia"])

# Mostrar la tabla
print(df.to_string(index=False))#Ignora el indice para mostrar una tabla más limpia

# Graficar la distribución de las frecuencias
suma_values = [item[0] for item in frecuencias_ordenadas]
frecuencia_values = [item[1] for item in frecuencias_ordenadas]

# Graficar el histograma de las frecuencias
plt.figure(figsize=(10, 6))
plt.bar(suma_values, frecuencia_values, color='skyblue')
plt.title('Distribución de la Suma de Tres Dados de 20 Caras')
plt.xlabel('Suma de los Dados')
plt.ylabel('Frecuencia')
plt.grid(True)

# Mostrar la gráfica
plt.show()
plt.close()
