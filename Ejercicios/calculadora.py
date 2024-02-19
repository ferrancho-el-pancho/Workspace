numero = int(input('Introduce el primer número de la operación: '))
numero_2 = int(input('Introduce el segundo número de la operación: '))
operacion = input('Introduce la operación aritmética (+, -, * o /): ')

while operacion not in ('*','+','-','/'):
    operacion = input('La operación aritmética que ha puesto no es correcta. Porfavor escriba otra: ')


if operacion == "*":
    result = numero * numero_2
    
elif operacion == "+":
    result = numero + numero_2
   
elif operacion == "-":
    result = numero - numero_2
    
else:
    result = numero / numero_2
    

print(f'El resultado de la operación aritmética de {numero} {operacion} {numero_2} es: {result}')
