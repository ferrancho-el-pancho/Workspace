def muestraDatos (datosEntrada):
    global media
    media = sum (datosEntrada)/len(datosEntrada)
    print(f'Puntuación media: {media}')
    print(f'Las puntuaciones va desde: ')
    print(f'{min(datosEntrada)} a {max(datosEntrada)}')



#Programa principal
media = 0
puntuaciones = [4,6,8,7,6,4,7,2,1,2,8,0,5]
titulo = 'Puntuaciones'
muestraDatos(puntuaciones)
print()
print(f'Puntuación media: {media}')