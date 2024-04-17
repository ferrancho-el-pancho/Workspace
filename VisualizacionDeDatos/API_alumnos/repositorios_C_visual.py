import requests

from plotly.graph_objs import Bar
from plotly import offline

# Realiza una llada a la API y guarda la respuesta.
url = 'https://api.github.com/search/repositories?q=language:C&sort=estrellas'
cabeceras = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=cabeceras)
print(f"Código de estado: {r.status_code}")

# Procesa los resultados.
diccionario_respuesta = r.json()


diccionarios_repositorios = diccionario_respuesta['items']
enlaces_repositorio, estrellas, etiquetas = [], [], []
for diccionario_repo in diccionarios_repositorios:
    nombre_repositorio = diccionario_repo['name']
    url_repositorio = diccionario_repo['html_url']
    enlace_repositorio = f"<a href='{url_repositorio}'>{nombre_repositorio}</a>"
    enlaces_repositorio.append(enlace_repositorio)

    estrellas.append(diccionario_repo['stargazers_count'])

    propietario = diccionario_repo['owner']['login']
    descripcion = diccionario_repo['description']
    etiqueta = f"{propietario}<br />{descripcion}"
    etiquetas.append(etiqueta)


# Crea la visualización.
datos = [{
    'type': 'bar',
    'x': enlaces_repositorio,
    'y': estrellas,
    'hovertext': etiquetas,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

mi_disposicion = {
    'title': 'Repositorios C mejor valorados en GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repositorio',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Estrellas',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': datos, 'layout': mi_disposicion}
offline.plot(fig, filename='reposiorios_C.html')
