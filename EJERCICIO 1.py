import numpy as np
import random


# 30 REPRESENTANTES
arreglo = np.zeros(30)

print("PROGRAMA QUE REALIZA UNA VOTACION ALEATORIA Y ORDENA LOS REPRESENTANTES ")
print("----------------------------------------------------------------------")

#VOTAR
for n in range(5000):
    numero_aleatorio = random.randint(0, 29)
    arreglo[numero_aleatorio]= arreglo[numero_aleatorio]+1

#print(arreglo)

# Ordenar los candidatos por número de votos
arreglo.sort()
representantes = np.argsort(arreglo)[::-1]

# Imprimir los resultados de la elección
for i in range(30):
    print(f"El representante numero {representantes[i]} obtuvo {int(arreglo[representantes[i]])} votos")
