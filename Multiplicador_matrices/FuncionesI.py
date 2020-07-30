
def leer_matriz(Num_matriz):
    f = int(input("Digite el número de filas de la "+str(Num_matriz)+" matriz:"))
    c = int(input("Digite el número de columnas de la "+str(Num_matriz)+" matriz:"))
    cantidad = f * c    
    return cantidad, f , c


def leer_consola(cantidad):
    
    print("Digite los {} números separados por una coma.".format(cantidad))
    a = input("Digite los números:")

    lista = []
    n = 0
    c = 0
    for i in a:
        if (i == ","):
            m = n 
            lista.append(a[c:m])
            c = m +1 
        n += 1 
    lista.append(a[c:len(a)])
        
    return lista


