import json

# Explora la estuctura de datos.
nombreFichero = 'datos/eq_data_1_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes = [], [], []
for diccionario_termometros in todos_los_diccionarios:
    magnitud = diccionario_termometros['properties']['mag']
    longitud = diccionario_termometros['geometry']['coordinates'][0]
    latitud = diccionario_termometros['geometry']['coordinates'][1]
    magnitudes.append(magnitud)
    longitudes.append(longitud)
    latitudes.append(latitud)

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes[:5])
