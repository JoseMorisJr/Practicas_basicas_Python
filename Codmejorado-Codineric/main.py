
import random

"""
Lanzar 4 dados y quedarme con la suma de los 3 mejores. 
"""
Cualidades = {"Fuerza":0,"Destreza":0,"Constitución":0,"Inteligencia":0,"Sabiduría":0,"Carisma":0}

def lanzar_dados():
        
    dados = [random.randint(1,6) for _ in range(4)]
        
    dados.sort(reverse=True)
    return sum(dados[:3])

for cualidad in Cualidades:
    Cualidades[cualidad] = lanzar_dados()
    print(cualidad +": "+str(Cualidades[cualidad]))
