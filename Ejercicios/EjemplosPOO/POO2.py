class Cuenta():
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar (self):
        print()
        print('Titular:',self.titular) 
        print('Cantidad:', self.cantidad)

    def ingresar (self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar (self, cantidad):
        if self.cantidad > 0:
            self.cantidad -= cantidad

        elif self.cantidad < 0:
            print('Estás en números rojos')

titular1 = Cuenta('Ferran Llach Folch', 100000)
titular2 = Cuenta('Sito', 2000)            


titular1.ingresar(100000)
titular1.retirar(200001)
titular1.mostrar()

titular2.retirar(500)
titular2.mostrar()