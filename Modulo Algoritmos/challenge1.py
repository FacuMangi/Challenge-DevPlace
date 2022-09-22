def esPrimo(numero):
    #Defino la funcion que sera usasda cuando se llame al programa
    for i in range(2, numero):
        #Creo un loop for para un rango del numero a analizar (este metodo range toma los naturales entre el 2 y el numero especificado en la funcion menos 1)
        if numero % i == 0: 
            #Como me basta saber si el numero es divisible por otro numero distinto de 1 y si mismo, ni bien se encuentre ese numero el loop se rompe y la variable x queda definida
            x = "no es primo"
            break
        else:
            #Si no se encontro un numero que rompa el loop significa que el numero a evaluar no tiene otros divisores mas que 1 y si mismo, se setea la variable x 
            x = "es primo"
    return x


dato = input("Ingrese un numero: ")
dato = int(dato)
y = esPrimo(dato)
#Dato es el numero ingresado por el usuario el cual pasa de ser un string a un valor numerico y llamo la funcion creada con ese dato
print(f"El numero {dato} {y}")
#Devuelvo el numero y la informacion recaudada