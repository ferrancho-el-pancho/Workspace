nombre = []
apellido = []
apodo = []

with open('Amigos.txt','r') as misAmigos:

	for amigo in misAmigos.readlines():

		amigo = amigo[0:-1]
		temp = amigo.split(" ")
		nombre.append(temp[0])
		apellido.append(temp[1])
		apodo.append(temp[2])

print(nombre)
print(apellido)
print(apodo)

