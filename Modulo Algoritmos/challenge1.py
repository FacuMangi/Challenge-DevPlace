def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0: 
            x = "no es primo"
            break
        else:
            x = "es primo"
    return x

dato = input("Ingrese un numero: ")
dato = int(dato)
y = esPrimo(dato)

print(f"El numero {dato} {y}")