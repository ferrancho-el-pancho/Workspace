import matplotlib.pyplot as plt

from camino_aleatorio import CaminoAleatorio

# Continua realizando nuevos caminos mientras que el programa esté activo.
while True:
    # Realiza un camino aleatorio.
    ca = CaminoAleatorio(50_000)
    ca.rellena_camino()

    # Dibuja los puntos en el camnino.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    num_puntos = range(ca.numero_de_puntos)
    ax.scatter(ca.valores_x, ca.valores_y, c=num_puntos, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Enfatiza el primer (verde) y último (rojo) puntos.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(ca.valores_x[-1], ca.valores_y[-1], c='red', edgecolors='none', s=100)

    # Elimina los ejes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    continua = input("¿Realizar otro camino? (s/n): ")
    if continua == 'n':
        break

# Reto: Movimiento molecular
'''
sustituye ax.scatter() por ax.plot(). Para simular el camino de un grano de polen
por la superficie de una gota de agua, pasa los argumentos ca.valores_x y ca.valores_y
e incluye el argumento linewidth: Usa 5.000 puntos en lugar de 50.000
'''