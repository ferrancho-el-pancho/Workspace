
colorOjos = ["azul","marrón","verde"]

with open('ojos.txt','w') as ficheroColorOjos:
	for cadaColor in colorOjos:
		ficheroColorOjos.write(cadaColor + ' ') 
