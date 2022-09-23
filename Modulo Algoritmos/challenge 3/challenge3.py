def calcular_importe(valor_hora, antig, horas_mes):
    #Defino la funcion que calcula el importe a pagar
    importe = valor_hora*horas_mes
    #El importe estandar a calcular
    if antig >= 10:
        #Condicional if en caso de que el usuario tenga mas de 10 años de antigüedad
        return importe + antig*30
        #Devuelve el importe mas el plus por antigüedad
    else:
        return importe
        #En caso de no tener mas de 10 años de antigüedad, devuelve solo el importe estandar


while True:
    valor_hora = int(input("Valor/Hora: "))
    #El usuario igresa el valor/hora de su trabajo
    #Cambio el tipo de dato de string a numerico

    nombre = input("Nombre: ")
    #El usuario igresa su nombre

    antig = int(input("Antigüedad: "))
    #El usuario igresa los años de antigüedad
    #Cambio el tipo de dato de string a numerico

    horas_mes = int(input("Horas trabajadas en el mes: "))
    #El usuario igresa las horas trabajadas en el mes
    #Cambio el tipo de dato de string a numerico

    importe = calcular_importe(valor_hora, antig, horas_mes)
    #Creo la variable importe que esta definida con lo que devuelve funcion calcularImporte con los parametros introduciods por el usuario
    print(f"\n Nombre: {nombre} \n Antigüedad: {antig} \n Importe: {importe}$")

    if input():
    #Cualquier input del usuario rompe el while Active y se cierra el programa
        break


