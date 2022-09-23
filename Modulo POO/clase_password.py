import random
import re #importo libreria de regular expressions operations para comparar en el metodo es_fuerte

class Password:
    """Representacion de password"""
    def __init__(self):
        """Constructor por defecto, con contraseña predefinida"""
        self.longitud = 8
        self.contraseña = '12345678'
    
    def __init__(self, longitud):
        """Constructor que usa longitud especificada y metodo de generar contraseña"""
        self.longitud = longitud
        self.contraseña = self.generar_password()

    def get_contraseña(self):
        """Getter para contraseña"""
        return self.contraseña
    
    def get_longitud(self):
        """Getter para longitud de contraseña"""
        return self.longitud
    
    def set_longitud(self, longitud):
        """Setter para longitud, genera una contraseña con longitud especificada"""
        self.longitud = longitud
        self.contraseña = self.generar_password()

    def set_contraseña(self, contraseña):
        """Setter para setear contraseña especificada, con longitud de la misma brindada"""
        self.contraseña = contraseña
        self.longitud = len(self.contraseña)
    
    def generar_password(self):
        """Generador de contraseña"""
        #Strings compuestos de los elementos que tendra la contraseña
        letter = 'abcdefghijklmnopqrstuvwxyz' 
        letters = letter + letter.upper()
        simbols = '!#$%&/()=+*-_?¿¡'
        numbers = '0123456789'

        #Sumo los strings y los transformo en una lista para usar el metodo shuffle y mezclar los elementos
        lista = list(letters + simbols + numbers)
        random.shuffle(lista)

        contra = ''
        #Para un i en un rango de longitud de contraseña deseado
        for i in range(self.longitud):
            #Toma un numero random dentro del rango 0, longitud de lista -1 para que no se rompa
            random_num = random.randint(0, len(lista) -1)
            #Suma elementos del lugar random en la lista mezclada 
            contra += str(lista[random_num])
        return contra

    def es_fuerte(self):
        """Metodo para verificar la fuerza de la contraseña"""
        #Use regular expressions operations para ver las coincidencias con los tipos de elementos que hay y si cumple con las minimas cantidades necesarias devuelve true
        uppercase = len(re.findall(r'[A-Z]',self.contraseña)) 
        lowercase = len(re.findall(r'[a-z]',self.contraseña))
        number = len(re.findall(r'[0-9]',self.contraseña))
        return (uppercase > 2  and lowercase > 1 and number > 3)