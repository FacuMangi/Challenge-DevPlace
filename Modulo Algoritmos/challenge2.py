def main():
    while True:
        contraseña = input('Escriba una contraseña: ')
        intentos = 1
        while intentos <= 3:
            dato = input(f'Escriba su contraseña: ')
            if dato != contraseña:
                print('Incorrecto, intente otra vez')
                intentos += 1

            if dato == contraseña:
                print('Felicitaciones, recordás tu contraseña')
                break
            
            if intentos > 3:
                print('Tenes que ejercitar la memoria')
        
        if input():
            break

if __name__ == '__main__':
    main()