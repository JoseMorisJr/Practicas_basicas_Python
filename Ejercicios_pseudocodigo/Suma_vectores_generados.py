
import random 
"""
Genere dos vectores de 100 elementos y sumelos uno a uno para obtener un nuevo 
vector de 100 elementos
"""

V1 = [random.randint(1,200) for _ in range(100)]
V2 = [random.randint(1,200) for _ in range(100)]

V3 = [(V1[i] + V2[i]) for i in range(100) ]

print("Vector 1 => \n", V1 )
print("Vector 2 => \n", V2 )
print("Vector 3 => \n", V3 )


"""
Genere dos vectores de 100 elementos y sume el primer valor con el ultimo valor, sucesivamente
hasta completar los 100 valores.
"""

# V4 = [(V1[i] + V2[99-i] ) for i in range(100)]

# print("Vector 4 => \n", V4 )