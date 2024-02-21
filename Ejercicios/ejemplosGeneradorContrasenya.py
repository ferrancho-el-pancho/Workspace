# Ejemplo 1
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
        print(temp1,temp2)
        palabra = temp2 + temp1
        return palabra

def cambiaTexto2(palabra):
    if palabra.lower() == palabra:
        return palabra.upper()
    elif palabra.upper() == palabra:
        return palabra.lower()
    else:
        return "mezclado"

def cambiaTexto3(palabra):
    longitud = 5 * len(palabra)
    palabra = str(longitud-5) + palabra + str(longitud)
    return palabra
#### Prueba 1
contrasenya = "votado"
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 2
contrasenya = "PELOTA"
contrasenya = cambiaTexto2(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 3
contrasenya = "Oculto"
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 4
contrasenya = "Gos"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 5
contrasenya = "xu"
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 6
contrasenya = "gnome"
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 7
contrasenya = "Bruv"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)

#### Prueba 8
contrasenya = "hard"
contrasenya = cambiaTexto3(cambiaTexto2(cambiaTexto1(contrasenya)))
print("La contraseña es: ",contrasenya)
