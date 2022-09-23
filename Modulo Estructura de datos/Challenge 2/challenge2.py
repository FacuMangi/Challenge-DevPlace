import clasePila 
pilaTemp = []

def reemplazar(pila, nuevo, viejo):
    #Siempre que la pila tenga elementos, se removera el primero y se comparara con el valor "viejo"
    while pila:
        x = pila.pop()
        #Si ese elemento es igual a "viejo", se agrega el "nuevo" elemento a una pila temporal
        if viejo == x:
            pilaTemp.append(nuevo)
        #Si no es igual a "viejo2, se agrega el elemento comparado a la pila temporal"
        else:
            pilaTemp.append(x)
    
    #Se traspasan los elementos de la pila temporal a la pila original
    while pilaTemp:
        j = pilaTemp.pop()
        pila.append(j)
    
    return pila

p = [1, 2, 4, 3, 5, 4, 2]
print(reemplazar(p, 9, 2))
