#Ejemplo del uso de funciones para reutilizar código

def muestraDatos (datosEntrada, mensaje):
    media = sum (datosEntrada)/len(datosEntrada)
    print(f'Media {mensaje} {media}')
    print(f'{mensaje} va desde: ')
    print(f'{min(datosEntrada)} a {max(datosEntrada)}')
    print()

#Programa principal
puntuaciones = [4,6,8,7,6,4,7,2,1,2,8,0,5]
titulo = 'Puntuaciones'
muestraDatos(puntuaciones, titulo)

lecturasPH = [3.4, 3.7,4.0, 3.2, 5.0, 2.7, 3.2]
texto = 'pH'
muestraDatos(lecturasPH, texto)

alturas = [154, 158, 187, 172, 155, 190, 182, 168]
palabra = 'Altura'
muestraDatos(alturas, palabra)