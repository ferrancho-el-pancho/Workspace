import random 
numero_1 = int(input("Dime el número mas alto: "))
numero_2 = int(input("Dime el número mas pequeño: "))
print(f'A ver si adivinas un número entre {numero_1} y {numero_2}')

numero = random.randrange(numero_2, numero_1+1)
mi_numero=int(input("Dime un número: "))
intentos = 1

while mi_numero != numero:

    if mi_numero < numero:
        mi_numero = int(input("No es el número correcto. El número es mas alto. Escribe uno nuevo: "))
        intentos += 1

    elif mi_numero > numero:
        mi_numero = int(input("No es el número correcto. El número es mas bajo. Escribe uno nuevo: "))
        intentos += 1


print(f'{mi_numero} es el número correcto. Has tardado {intentos} intentos.')
