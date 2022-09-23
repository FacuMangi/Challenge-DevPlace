#Defino la funcion con una lista de argumento
def suma_recur(listaNum):
    #Si la lista tiene solo un elemento, me devuelve ese elemento
    if len(listaNum) == 1:
        return listaNum[0]
    #Si la lista tiene mas de un elemento
    else:
        #Devuelve la suma de ese primer elemento y otro que viene de llamar a la funcion con una lista comprendida por los elementos desde el segundo en adelante
        return listaNum[0] + suma_recur(listaNum[1:]) #Asi con cada llamado la lista se achica y se agregan mas elementos a la suma

listaNumeros = [1, 2, 3, 4, 5]

print(f"Suma: {suma_recur(listaNumeros)}")