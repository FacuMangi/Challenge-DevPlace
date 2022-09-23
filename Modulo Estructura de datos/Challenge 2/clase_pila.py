class Pila:
    """Representacion de una Pila, que puede apilar, desapilar y verificar si esta vacia."""
    def __init__(self):
        """Crea una pila vacia."""
        self.items=[]
    
    def apilar(self, x):
        """Agrega x a la pila."""
        self.items.append(x)
    
    def desapilar(self):
        """Devuelve el elemento de arriba de la pila.
            Si la pila esta vacia da una excepcion."""
        try:
            return self.pop()

        except IndexError:
            raise ValueError("Pila vacia")
    
    def es_vacia(self):
        """Devuelve True si la lista esta vacia, False si no lo esta"""
        return self.items == []
    
