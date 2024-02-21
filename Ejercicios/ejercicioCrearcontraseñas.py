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

def cambiaTexto4(palabra):
    