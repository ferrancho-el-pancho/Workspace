def calculoInteres(prestamo, periodo, interes):
    total = prestamo
    for años in range(periodo):
        total *= (1+interes/100)
    return (total)

#Programa principal 
cantidad = int(input('Introduce la cantidad prestada: '))
años = int(input('Introduce la duración del prestamo en años: '))
interes = float(input('Introduce el interés: '))
print(f'Cantidad resultante {round(calculoInteres(cantidad, años, interes),2)}€')