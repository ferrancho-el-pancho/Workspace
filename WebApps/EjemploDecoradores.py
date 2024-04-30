import time

def calcularTiempo(funcion):

    def funcionModificada(n):
        inicio =time.time()
        funcion(n)
        final = time.time()
        print (f'Tiempo de ejecución: {final - inicio} segundos')

    return funcionModificada

@calcularTiempo
def imprimirNumeros(n):
    #inicio = time.time ()
    for i in range(n):
        print(i)
    #final = time.time ()
    #print(f'Tiempo de ejecución: {final - inicio}')

@calcularTiempo
def suma(a):
    return a + 100
@calcularTiempo
def resta (a):
    return a - 100

imprimirNumeros(1000)
suma (1000)
resta(1000)