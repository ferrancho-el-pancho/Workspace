from plotly.graph_objs import Bar, Layout
from plotly import offline

from dado import Dado

# Crea un D6.
dado = Dado()

# Realiza varios lanzamientos y guarda los resultados en una lista.
resultados = []
for lanzamiento_num in range(100):
    resultado = dado.lanza()
    resultados.append(resultado)

    
# Analiza los resultados.
frecuencias = []
for valor in range(1, dado.num_caras+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)



    
# Visualiza los resultados.
valores_x = list(range(1, dado.num_caras+1))
datos = [Bar(x=valores_x, y=frecuencias)]

config_eje_x = {'title': 'Resultado'}
config_eje_y = {'title': 'Frecuencia del Resultado'}
mi_disposicion = Layout(title='resultados de lanzar un D6 1000 veces',
        xaxis=config_eje_x, yaxis=config_eje_y)
offline.plot({'data': datos, 'layout': mi_disposicion}, filename='d6.html')
