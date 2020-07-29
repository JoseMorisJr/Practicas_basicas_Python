
"""
Código para invertir un vector y mostrar sus elementos
"""
import random 
import array
import copy

a = array.array("I",[random.randint(1,20) for _ in range(50) ])

print("Vector original:\n ",list(a))
c = copy.copy(a[::-1])
print("Vector invertido:\n ",list(c))