from random import choice

'''
Esta clase tomará decisiones aleatorias sobre la dirección que debería llevar el camino.
Necesita tres atributos: una variable para almacenar el número de puntos del camino y
dos listas para guardar los valores de coordenadas x e y de cada punto del camino.
'''

class CaminoAleatorio:
    """Una clase para generar caminos aleatorios."""
    
    def __init__(self, numero_de_puntos=5000):
        """Inicializa los atributos de un camino."""
        self.numero_de_puntos = numero_de_puntos
        
        # Todos los caminos empiezan en (0, 0).
        self.valores_x = [0]
        self.valores_y = [0]

    def rellena_camino(self):
        """Calcula todos los puntos en el camino."""
    
        # Continua dando pasos hasta que el camino alcance la longitud deseada.
        while len(self.valores_x) < self.numero_de_puntos:
        
            # Decide en qué dirección ir y hasta donde llegar en esa dirección which direction.
            # 1--> derecha, -1 --> izquierda
            direccion_x = choice([1, -1])
            # Decide hasta donde llegar en direccion x
            distancia_x = choice([0, 1, 2, 3, 4])
            paso_x = direccion_x * distancia_x
        
            # 1--> arriba, -1 --> abajo
            direccion_y = choice([1, -1])
            # Decide hasta donde llegar en direccion y
            distancia_y = choice([0, 1, 2, 3, 4])
            paso_y = direccion_y * distancia_y
        
            # Rechaza movimientos que no van a ningún lado.
            if paso_x == 0 and paso_y == 0:
                continue
        
            # Calcula la nueva posición sumando los valores actuales a los últimos almacenados y los añadimos a las respectivas listas.
            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y
        
            self.valores_x.append(x)
            self.valores_y.append(y)
