def calculadora(num1, num2, oper):

    if oper == "*":
        result = num1 * num2
    
    elif oper == "+":
        result = num1 + num2
   
    elif oper == "-":
        result = num1 - num2
    
    else:
        result = num1 / num2
    
    return result
    



numero = int(input('Introduce el primer número de la operación: '))
numero_2 = int(input('Introduce el segundo número de la operación: '))
operacion = input('Introduce la operación aritmética (+, -, * o /): ')

while operacion not in ('*','+','-','/'):
    operacion = input('La operación aritmética que ha puesto no es correcta. Porfavor escriba otra: ')


print(f'El resultado de la operación aritmética de {numero} {operacion} {numero_2} es: {calculadora(numero, numero_2, operacion)}')
