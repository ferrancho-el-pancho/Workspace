letraDNI = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
DNI = int(input('Dime tu DNI sin la letra: '))
print(f'Posicion en la lista: {DNI%23}')

print(f'La letra para el DNI {DNI} es: {letraDNI[DNI%23]}')