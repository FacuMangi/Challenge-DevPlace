def main():
    while True:
    #El loop while True es para poder dejar de ejecutar el programa una vez se realicen los intentos
        contraseña = input('Escriba una contraseña: ')
        #Setea la contraseña a recordar
        intentos = 1
        #Seteo los intentos en 1, ya que sera el primer intento
        while intentos <= 3:
            #Mientras los intentos sean menor o igual a 3, la computadora seguira pidiendo la contraseña 
            dato = input(f'Escriba su contraseña: ')
            if dato != contraseña:
                #Si la contraseña ingresada no es igual a la contraseña seteada previamente se suma un intento a la cuenta de intentos
                print('Incorrecto, intente otra vez')
                intentos += 1

            if dato == contraseña:
                #Si la contraseña ingresada es igual a la contraseña seteada al principio se rompe el loop
                print('Felicitaciones, recordás tu contraseña')
                break
            
            if intentos > 3:
                #Si los intentos son mas de 3 se imprime el mensaje correspondiente
                print('Tenes que ejercitar la memoria')
        
        if input():
            #Con cualquier input del usuario se rompe el while Active y se cierra el programa, ya sea que el usuario haya recordado su contraseña o no
            break

if __name__ == '__main__':
    main()