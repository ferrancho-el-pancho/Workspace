numero = int(input("Introduce el número: "))
suma_acutal = 0
mult_3_actual = 0
print(f'M = {mult_3_actual}: S = {suma_acutal}')

while suma_acutal < numero:
    mult_3_actual += 3
    suma_acutal += mult_3_actual
    print(f'M={mult_3_actual:2d}: S={suma_acutal:2d}')