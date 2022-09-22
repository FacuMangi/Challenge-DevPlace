def calcularImpote(valorHora, antig, horasMes):
    importe = valorHora*horasMes
    if antig >= 10:
        return importe + antig*30
    else:
        return importe


while True:
    valorHora = input("Valor/Hora: ")
    valorHora = int(valorHora)

    nombre = input("Nombre: ")

    antig = input("Antigüedad: ")
    antig = int(antig)

    horasMes = input("Horas trabajadas en el mes: ")
    horasMes = int(horasMes)

    importe = calcularImpote(valorHora, antig, horasMes)
    print(f"\n Nombre: {nombre} \n Antigüedad: {antig} \n Importe: {importe}$")

    if input():
    #Si el usuario escribe algo se rompe el while Active y se cierra el programa
        break


