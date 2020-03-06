import numpy as np
import random

def duplic(a, tamano):
    print("duplicados: ")
    for i in range(0, tamano):
        for j in range(i + 1, tamano):
            if a[i] == a[j]:
                print(a[i])

a = np.random.randint(10, size=(10))

print("mi lista: ",a)
tamano = len(a)
#print(tamano)

b = a
b.sort()
print("Ordenada: ",b)

#duplic(a, tamano)




