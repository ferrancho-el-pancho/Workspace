from plotly.graph_objs import Bar, Layout
from plotly import offline

from dado import Dado

# Crea dos dados D6.
dado1 = Dado()
dado2 = Dado()
dado3 = Dado()

# Realiza varios lanzamientos y guarda los resultados en una lista.
resultados = []
for lanzamiento_num in range(1000):
    resultado = dado1.lanza() + dado2.lanza() + dado3.lanza()
    resultados.append(resultado)
    
# Analiza los resultados.
frecuencias = []
maximo_resultado = dado1.num_caras + dado2.num_caras + dado3.num_caras
for valor in range(3, maximo_resultado+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)
    
# Visualiza los resultados.
valores_x = list(range(3, maximo_resultado+1))
datos = [Bar(x=valores_x, y=frecuencias)]

config_eje_x = {'title': 'Resultado', 'dtick': 1}
config_eje_y = {'title': 'Frecuencia del Resultado'}
mi_disposicion = Layout(title='resultados de lanzar dos dados D6 1000 veces',
        xaxis=config_eje_x, yaxis=config_eje_y)
offline.plot({'data': datos, 'layout': mi_disposicion}, filename='3xd6.html')
