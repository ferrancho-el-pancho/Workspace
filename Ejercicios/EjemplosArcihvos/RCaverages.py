import statistics
nombre = input('Porfavor introduce un nombre: ')
marcas = []
suma = 0

with open('RCaverages.csv','r') as Alumnos:
	for alumno in Alumnos.readlines():
		alumno = alumno[0:-1]
		temp = alumno.split(",")
		if temp [0] == nombre: 
			marcas.append(float(temp[1]))
print(f'Las marcas para {nombre} son: ')

for i in range(len(marcas)):
	print(marcas[i])

#media = sum(marcas)/len(marcas)
	
print(f'La media de las marcas de {nombre} es {statistics.mean(marcas)}')