
import random 
"""
En un arreglo de 15 filas por 12 columnas, halle el menor valor del arreglo, 
sumar los valores de las 5 primeras filas, y el total de elementos negativos
en las columnas desde la 5ta hasta la 9na
"""

arr = []
for _ in range(15):
    arr.append([int(random.randint(-100,100)) for __ in range(12)])
print(arr)

#minimo
minimo = min(min(arr))

#suma
arr_sum = []
[arr_sum.append(i[j])for i in arr[:5] for j in range(12)]
suma = sum(arr_sum)

#total
arr_neg = []
[arr_neg.append(i[j]) for i in arr[:] for j in range(4,9) if i[j]<0]

neg = len(arr_neg)

print("\nMenor elemento del arreglo: %i"%(minimo))
print("Suma de las primeras 5 filas: %i"%(suma))
print("Cantidad de negativos de columna 5 hasta 9: %i"%(neg))