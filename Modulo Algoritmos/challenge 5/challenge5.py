numeros = []

while True:
    numero = int(input('Ingrese un numero: '))
    if numero == -1:
        break
    
    numeros.append(numero)

print(numeros)