#C:/Anadonda/python.exe
import numpy as np
from FuncionesI import *

print("########## BIENVENIDO AL MULTIPLICADOR DE MATRICES ##########")
print("Solo se permite operar dos matrices.")
print("Recuerde que la cantidad de columnas de la primera matriz debe de ser \
igual al número de filas de la segunda matriz.")

cantidad1, f1,c1 = leer_matriz('primera')
cantidad2, f2 ,c2 = leer_matriz('segunda')

while (c1 != f2):
    print("Las matrices no se pueden multiplicar.")
    print("Vuelva a intentarlo.")    
    cantidad1, f1,c1 = leer_matriz('primera')
    cantidad2, f2 ,c2 = leer_matriz('segunda')

print("PRIMERA MATRIZ")
matriz1 = leer_consola(cantidad1)

while (cantidad1 != len(matriz1)):
    print("Ocurrio un error al digitar los números vuelva a intentarlo")
    matriz1 = leer_consola(cantidad1)

print("SEGUNDA MATRIZ")
matriz2 = leer_consola(cantidad2)

while (cantidad2 != len(matriz2)):
    print("Ocurrio un error al digitar los números vuelva a intentarlo")
    matriz2 = leer_consola(cantidad2)

matriz1 = np.array(matriz1,dtype="int").reshape(f1,c1)
matriz2 = np.array(matriz2,dtype="int").reshape(f2,c2)

fR , cR = f1 , c2

R = np.zeros((fR,cR),dtype="int")

for i in range(0,fR):
    for j in range(0,cR):
        for k in range(0,c1):
            R[i,j] += (matriz1[i,k] * matriz2[k,j]) 

print("LA MATRIZ RESULTANTE ES:")
print(R)