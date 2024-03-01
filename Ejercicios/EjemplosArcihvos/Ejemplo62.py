
nombres = []

with open('Amigos.txt','r') as misAmigos:

    for amigo in misAmigos.readlines():

        amigo = amigo[0:-1]
        temp = amigo.split(" ")
        nombres.append(temp)

print(nombres)
