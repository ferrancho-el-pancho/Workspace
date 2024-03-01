
colorPelo = ["marron","pelirojo","blanco","oscuro","rubio"]

with open('ojos.txt','a') as ficheroColorPelo:
	for color in colorPelo:
		ficheroColorPelo.write(color+"\n")
