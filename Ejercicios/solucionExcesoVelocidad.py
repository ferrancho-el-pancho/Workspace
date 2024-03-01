## La siguiente función verifica si el archivo existe y luego lee
## todos los datos del archivo y lo carga en una lista. 
## La lista se devuelve al programa principal.
def leerFichero():
    datos = []

    ## Primero abre una conexión 'append' al archivo. Esto provoca que
    ## si el archivo no existe, el programa creará un archivo nuevo.
    ## Ten en cuenta que si se abriera una conexión de 'escritura', el contenido del
    ## archivo se eliminaria.
    with open('velocidades.txt','a') as comprueba:
        print("Comprobando fichero . . . ")

    ## Leer los datos anteriores del archivo. Si el archivo está vacío
    ## se devolverá una lista vacía.
    with open('velocidades.txt','r') as todo:
        for each in todo.readlines():
            datos.append(each[0:-1])
    return datos


## Las siguientes funciones extraen la antigüedad y la velocidad, 
## devolviendo dos listas de datos separadas.
def extraeAntiguedad(datosVelocidades):
    antiguedadesVehiculos = []
    temp = []
    for each in datosVelocidades:
        temp = each.split(",")
        antiguedadesVehiculos.append(int(temp[0]))
    return antiguedadesVehiculos

def extraeResultados(datosVelocidades):
    resultadosVehiculos = []
    temp = []
    for each in datosVelocidades:
        temp = each.split(",")
        resultadosVehiculos.append(int(temp[1]))
    return resultadosVehiculos


## Este procedimiento calcula el número de vehículos y el número de esos
## vehículos que no respetaron el límite de velocidad. Estos valores pueden ser
## utilizados para calcular y mostrar el porcentaje de vehículos que superaban 
## el exceso de velocidad.
def muestraPorcentaje(resultadosVehiculos):
    totalVehiculos = len(resultadosVehiculos)
    totalFallos = sum(resultadosVehiculos)
    porcentaje = 100 / totalVehiculos * totalFallos
    print(f"Exceso de velocidad - {round(porcentaje,2)}%")
    print(f"Velocidad correcta - {round(100-porcentaje, 2)}%")


## Esta función recorre los datos del vehículo y utiliza una lista separada para
## mantener un total del número de errores para cada antigüedad del vehículo.
## Ten en cuenta que, además de mostrar el resultado requerido, la nueva lista se
## devuelve tal como está, ya que es necesaria en el siguiente procedimiento.
def muestraFallosPorAntiguedad(antiguedadesVehiculos,resultadosVehiculos):
    superaVelocidadPorAntiguedad = [0]*120

    for vuelta in range(len(antiguedadesVehiculos)):
        ## Si se detectó que un vehículo superó el límite de velocidad.
        if resultadosVehiculos[vuelta] == 1:
            ## La siguiente línea utiliza la antigüedad de cada vehículo como índice de lista.
            ## Ten en cuenta que a medida que las edades comienzan en 1 y los índices de lista comienzan
            ## en 0 las edades se compensan con -1 (los vehículos de 1 año se almacenan
            ## en el índice 0, 2 años en el 1 y así sucesivamente).
            superaVelocidadPorAntiguedad[antiguedadesVehiculos[vuelta]-1] += 1

    for vuelta in range(max(antiguedadesVehiculos)):
        ## Muestra los totales de automóviles a alta velocidad para cada antigüedad. Recordando
        ## contabilizar el desplazamiento (vuelta+1).
        print(vuelta+1,"-",superaVelocidadPorAntiguedad[vuelta])

    return superaVelocidadPorAntiguedad


## Este procedimiento encuentra el valor máximo en la lista de totales de exceso de velocidad y
## luego encuentra el índice de este valor. El índice se utiliza luego para mostrar
## la antigüedad del vehículo que fue sorprendido circulando a mayor velocidad (indice+1).
def superaVelocidadMasFrecuente(superaVelocidadPorAntiguedad):
    peor = superaVelocidadPorAntiguedad.index(max(superaVelocidadPorAntiguedad)) + 1
    print(f"Vehículos de {peor} años fueron los que más superaron el límite de velocidad.")
       

## El procedimiento final escribe los datos completos de velocidad del vehículo en el
## archivo. Ten en cuenta que como se leyeron los datos guardados, los datos del archivo deben
## completamente sobrescritos con los datos antiguos y nuevos.
def escribeDatosFichero(antiguedadesVehiculos,resultadosVehiculos):
    with open('velocidades.txt','w') as ficheroVehiculos:
        for vuelta in range(len(antiguedadesVehiculos)):
            ficheroVehiculos.write(str(antiguedadesVehiculos[vuelta])+","+str(resultadosVehiculos[vuelta])+"\n")


## PROGRAMA PRINCIPAL

## Obten cualquier dato previamente almacenado.
datosVelocidades = []
datosVelocidades = leerFichero()

## Las dos funciones siguientes extraen las antigüedades de los vehículos y los resultados de exceso de velocidad.
## a partir de los datos del archivo, almacenando las edades y los resultados de exceso de velocidad en dos listas paralelas.
## ** Ver notas extras al final **
antiguedades = []
resultados = []
antiguedades = extraeAntiguedad(datosVelocidades)
resultados = extraeResultados(datosVelocidades)

## Obten nuevos datos del usuario.
nuevaEdad = 0
while nuevaEdad != 999:
    nuevaEdad = int(input("Por favor introduce la antigüedad del vehículo nuevo: "))
    if nuevaEdad != 999:
        while nuevaEdad < 1 or nuevaEdad > 120:
            nuevaEdad = int(input("Por favor introduce una antigüedad entre 1 y 120: "))
        antiguedades.append(nuevaEdad)

        speedResult = int(input("Por favor introduce el resultado de superación de velocidad: "))
        while speedResult < 0 or speedResult > 1:
            speedResult = int(input("Por favor re-introduce un resultado válido de superación de velocidad 1 o 0: "))
        resultados.append(speedResult)

## Llama a un procedimiento para mostrar el porcentaje de errores.
muestraPorcentaje(resultados)

## Llama a un procedimiento para mostrar el numero de vehículos de cada edad que superaron
## el límite de velocidad.
totalesSuperanVelocidad = []
totalesSuperanVelocidad = muestraFallosPorAntiguedad(antiguedades,resultados)

## Utilizando la lista creada anteriormente, llama a un procedimiento para mostrar la antigüedad del
## vehículo que superó con mayor frecuencia el límite de velocidad.
superaVelocidadMasFrecuente(totalesSuperanVelocidad)

## Finalmente pasa los datos a un procedimiento que actualizará los datos almacenados.
escribeDatosFichero(antiguedades,resultados)


## ** Notas adicionales
## 1. La respuesta de ejemplo se ha escrito para mostrar una solución con dos
## listas separadas que almacenan los datos. Podría haber sido fácilmente
## escrito usando una lista 2D.
## 2. Las funciones de Python pueden devolver y asignar más de un valor. En este programa
## se han utilizado dos funciones separadas para devolver las dos listas una cada vez.

