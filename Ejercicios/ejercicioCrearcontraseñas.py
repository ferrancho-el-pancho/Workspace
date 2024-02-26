import random


def cambiaTexto1(palabra):
    longitudPalabra = len(palabra)
    if longitudPalabra <=2:
        return palabra
    elif longitudPalabra>2 and longitudPalabra<=6:
        temp1 = palabra[0:2]
        temp2 = palabra[len(palabra)-2:]
        palabra = temp2 + palabra + temp1
        return palabra
    else:
        temp1 = palabra[0:3]
        temp2 = palabra[len(palabra)-3:]
        #print(temp1,temp2)
        palabra = temp2 + temp1
        return palabra

def cambiaTexto2(palabra):
    if palabra.lower() == palabra:
        return palabra.upper()
    elif palabra.upper() == palabra:
        return palabra.lower()
    else:
        palabra = palabra[4:] + palabra[:4]
        return palabra

def cambiaTexto3(palabra):
    longitud = 5 * len(palabra)
    palabra = str(longitud-5) + palabra + str(longitud)
    return palabra

def cambiaTexto4(palabra):
    simbolos = ['*', '@', '$', '#', '_', '-', '/', 'º', 'ª', '&', '%', '€', '.', ',']
    numero1 = random.randrange(1, 4+1)
    numero2 = random.randrange(1, 4+1)
    numero3 = random.randrange(1, 4+1)
    numero4 = random.randrange(1, 4+1)
    numero5 = random.randrange(1, 4+1)
    palabra = palabra[0:1] + simbolos[numero1] + palabra[1:3] + simbolos[numero3] + palabra[3:4] + simbolos[numero2] + palabra[4:6] + simbolos[numero4] +palabra[6:8] + simbolos[numero5] + palabra[8:]
    return palabra


contrasenya = input('Introduce una palabra: ')
numero = random.randrange(1, 2+1)
print (f'El número aleatorio es: {numero}')

if numero == 1:
    contrasenya = cambiaTexto2(cambiaTexto3(cambiaTexto1(cambiaTexto4(contrasenya))))
   
elif numero == 2:
    contrasenya = cambiaTexto1(cambiaTexto3(cambiaTexto4(contrasenya)))
   
else:
    contrasenya = cambiaTexto1(cambiaTexto3(cambiaTexto4(contrasenya)))
  

if len(contrasenya) < 10:
    contrasenya = contrasenya + contrasenya

elif len(contrasenya) > 10:
    contrasenya = contrasenya[0:10]

else:
    contrasenya = contrasenya

print(f'Tu contraseña es: {contrasenya[0:10]}')