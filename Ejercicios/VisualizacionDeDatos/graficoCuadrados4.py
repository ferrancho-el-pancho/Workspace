import matplotlib.pyplot as plt


valores=[1,2,3,4,5]
cuadrados=[1,4,9,16,25]

# Utilizamos estilos integrados: (con el intérprete de python)
# >>> import matplotlib.pyplot as plt 
# >>> plt.style.available
'''
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 
'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
 
'''
plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
ax.plot(valores, cuadrados, linewidth=3)

# Establece el título del gráfico y las etiquetas de los ejes
ax.set_title("Cuadrados de los números", fontsize=18)
ax.set_xlabel("Valor", fontsize=12)
ax.set_ylabel("Cuadrado del valor", fontsize=12)

# Establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(axis='both', labelsize=12)

plt.show()

# Si queremos guardar las gráficas automáticamente:
#plt.savefig('graficoCuadrados.png', bbox_inches='tight')
fig.savefig('graficoCuadrados.png')

