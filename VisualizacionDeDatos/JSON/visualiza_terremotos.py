import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explora la estuctura de datos.
nombreFichero = 'datos/eq_data_30_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes, textos_hover = [], [], [], []
for diccionario_termometros in todos_los_diccionarios:
    titulo = diccionario_termometros['properties']['title']
    magnitudes.append(diccionario_termometros['properties']['mag'])
    longitudes.append(diccionario_termometros['geometry']['coordinates'][0])
    latitudes.append(diccionario_termometros['geometry']['coordinates'][1])
    textos_hover.append(diccionario_termometros['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': textos_hover,
    'marker': {
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitud'},
    }

}]


mi_disposicion = Layout(title = 'Terremotos Globales')

fig = {'data':data, 'layout': mi_disposicion}
offline.plot(fig, filename = 'terremotos_globales.html')