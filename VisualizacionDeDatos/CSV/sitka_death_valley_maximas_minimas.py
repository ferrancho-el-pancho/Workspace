import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero1 = 'datos/death_valley_2018_simple.csv'
nombreFichero2 = 'datos/sitka_weather_2018_simple.csv'

with open(nombreFichero1) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas maximas del fichero.
    fechas, maximas1, minimas1 = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        maxima = int(fila[4])
        maximas1.append(maxima)
        minima = int(fila[5])
        minimas1.append(minima)



with open(nombreFichero2) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas maximas del fichero.
    maximas2, minimas2 = [], []
    for fila in lector:
        maxima = int(fila[5])
        maximas2.append(maxima)
        minima = int(fila[6])
        minimas2.append(minima)
 




# Dibuja las temperaturas maximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.axis ([17545, 17900, 20, 150])
ax.plot (fechas, maximas1, c='red')
ax.plot (fechas, minimas1, c='blue')
ax.plot (fechas, maximas2, c='orange')
ax.plot (fechas, minimas2, c='green')


#sombrea el área entre la líneas
plt.fill_between(fechas, maximas1, minimas1, facecolor='purple', alpha = 0.5)
plt.fill_between(fechas, maximas1, minimas1, facecolor='black', alpha = 0.5)




# Formatea el gráfico.
plt.title("Temperaturas diarias maximas y mínimas - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

