# Creo una lista vacia
L = []

#Defino la funcion que va a usar los input del usuario
def funcion(i, n):
    # Ingresando los elementos hasta que se cumpla el rango
    for i in range(0, i):
        elementos = int(input())
    
        # Añado el elemento
        L.append(elementos) 

    # Devuelve la lista con todos los elementos menos aquellos que tengan el mismo valor que n 
    return ([i for i in L if i != n])

# Numero de elementos a ingresar
i = int(input("Ingresar cantidad de elementos en la lista: "))
# Elemento de la lista a retirar
n = int(input("n = ") )

x = funcion(i, n)
print (x)