tabla_mult = int(input("Dime el número para calcular la tabla de multiplicar: "))
for factor_mul in range (1, 11):
    resultado = tabla_mult * factor_mul
    print (f'{tabla_mult} * {factor_mul} = {resultado}')