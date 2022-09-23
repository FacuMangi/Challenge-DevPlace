from clase_password import Password

contra_usuario = input('Ingrese contraseña: ')

objeto_contra = Password()
objeto_contra.set_contraseña(contra_usuario)

if objeto_contra.es_fuerte:
    print(f'Su contraseña {contra_usuario} es fuerte')
else:
    print(f'Su contraseña {contra_usuario} no es tan fuerte')