import csv
import matplotlib.pyplot as plt

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)
    #print(fila_cabecera)
    temperaturas_maximas = []
    for fila in lector:
        maxima = int(fila[5])
        temperaturas_maximas.append(maxima)
    
    #print (temperaturas_maximas[:10])


valores = temperaturas_maximas
ax = plt.subplot()
ax.plot(valores, c='red')

ax.set_title('Temperaturas máximas ºF', fontsize=18)
ax.set_ylabel('Temperaturas', fontsize=18)
ax.set_xlabel('Medidas', fontsize = 18)

plt.show()
