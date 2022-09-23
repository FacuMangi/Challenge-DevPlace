from random import randint
#Importo de random el metodo randint que devuelve un numero aleatorio dado un determinado rango

def main():
    rand_num = randint(0, 1000)
    #Se genero el numero
    print('Se genero un numero entre 0 y 1000. ¿Que numero es?')
    #Devuelve el mensaje al usuario

    while True:
        #Se crea el loop que permite intentar todas las veces que el usuaario quiera
        intento = input('> ')
        #Input del intento en modo de string
        intento = int(intento)
        #Cambio el tipo de dato de string a numerico
        
        if intento == rand_num:
            break
        if intento < rand_num:
            print('Es mayor')
        if intento > rand_num:
            print('Es menor')
        #Si el usuario acierta se cierra el programa, de lo contrario devuelve las pistas dependiendo de la comparacion entre el intento y el numero

if __name__ == '__main__':
    main()
#Condicion que llama la funcion main 