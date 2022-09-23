numeros = []

while True:
    numero = int(input('Ingrese un numero: '))
    if numero == -1:
        break
    
    numeros.append(numero)

numeros.sort()
print(f"Mayor numero introducido: {numeros[-1]}")
print(f"Menor numero introducido: {numeros[0]}")
print(f"Cantidad de numeros introducidos: {len(numeros)}")
print(f"Suma total de los numeros introducidos: {sum(numeros)}")