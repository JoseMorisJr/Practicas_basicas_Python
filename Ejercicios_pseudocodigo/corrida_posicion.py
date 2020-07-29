
"""
Leer un vector y hacer que el primer elemento pase a la segunda posición,
el segundo elemento a la tercer posición, ..., el último elemento a la primera posicición
"""
import random 
import array


a = array.array("I",[random.randint(1,20) for _ in range(3) ])
b = array.array("I",[0])

[b.insert((i+1),a[i])for i in range(len(a)-1)]
b[0] = a[-1]
print("La matriz contiene estos elementos: \n",list(a))
print("La nueva matriz contiene estos elementos: \n",list(b))

