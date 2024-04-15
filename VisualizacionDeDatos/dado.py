from random import randint

class Dado:
    """Una clase que representa un único dado."""
    
    def __init__(self, num_caras=6):
        """Asume un dado de 6 caras."""
        self.num_caras = num_caras
        
    def lanza(self):
        """"Devuelve un número aleatorio entre 1 y el número de caras."""
        return randint(1, self.num_caras)
