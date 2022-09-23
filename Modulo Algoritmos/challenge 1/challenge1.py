def es_primo(numero):        
    #Defino la funcion que sera llamada cuando se ejecute el programa
    for i in range(2, numero):
        #Creo un loop for para un rango dado por el numero a analizar (este funcion range toma los naturales entre el 2 y el numero especificado en la funcion menos 1)
        if numero % i == 0: 
            #Como me basta saber si el numero es divisible por otro numero distinto de 1 y si mismo, ni bien se encuentre ese numero el loop se rompe y la variable x queda definida
            x = "no es primo"
            break
        else:
            #Si no se encontro un numero que rompa el loop significa que el numero a evaluar no tiene otros divisores mas que 1 y si mismo, se setea la variable x 
            x = "es primo"
    return x


while True:
#El lpop while True me permite mantener el programa corriendo hasta que se ejecuten todas las funciones
    dato = input("Ingrese un numero: ")
    #Dato es el numero ingresado por el usuario el cual pasa de ser un string a un valor numerico y llamo la funcion creada con ese dato
    dato = int(dato)
    #Cambio el tipo de dato de string a numerico
    y = es_primo(dato)     
    #Llamo la funcion con el parametro dato  
    print(f"El numero {dato} {y}")
    #Devuelvo el numero y la informacion recaudada
    
    if input():
        break
    #Rompe el loop while cuando el usuario introduce un input cualquiera





