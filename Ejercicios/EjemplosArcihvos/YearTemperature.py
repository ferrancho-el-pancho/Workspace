
def leeFichero(nombreFichero):
    lineas = []
    nombreFichero = nombreFichero + ".csv"
    with open(nombreFichero,'r') as todo:
        for each in todo.readlines():
            lineas.append(each[0:-1])
    return lineas

def calculaMedia(temperaturas,inicio,final):
    temp = []
    total = 0

    for cadaSemana in range(inicio-1,final):
        temp = temperaturas[cadaSemana].split(",")
        temp.pop(0)
        for loop in range(7):
            total = total + int(temp[loop])

    media = total / ((final+1-inicio)*7)
    print("La temperatura media para las semanas ",inicio,"hasta",final)
    print(round(media,2)," grados")

## PROGRAMA PRINCIPAL
semanas = []

fichero = "yearTemperatures"
semanas = leeFichero(fichero)


primera = int(input("Por favor introduce la semana inicial "))
while primera < 1:
    primera = int(input("Please vuelve a introducir la semana inicial "))

segunda = int(input("Por favor introduce la semana final "))
while segunda > 52 or segunda < primera:
    segunda = int(input("Por favor vuelve a introducir la semana final "))

calculaMedia(semanas,primera,segunda)
