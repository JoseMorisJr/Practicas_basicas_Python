
import random
"""
Crea dos matrices de 12x12 y compara si sus diagonales principales 
son iguales
"""

#creando matrices de 12x12

M1 = [] ; M2 = []
for _ in range(12):
    M1.append([random.randint(1,100) for _ in range(12)])
    M2.append([random.randint(1,100) for _ in range(12)])

#Volviendo a la diagonal igual
# for i in range(12): M2[i][i] = M1[i][i] 

#Comparando los valores de la diagonales 

D_M1 = [M1[i][i]for i in range(12)] 
D_M2 = [M2[i][i]for i in range(12)] 

DV = [True if (D_M1[i] == D_M2[i]) else False for i in range(12)] 

print("Las diagonales son iguales" if all(DV) else "Las diagonales no son iguales" )

