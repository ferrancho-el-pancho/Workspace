import matplotlib.pyplot as plt

cuadrados=[1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(cuadrados, linewidth=3)

# Establece el título del gráfico y las etiquetas de los ejes
ax.set_title("Cuadrados de los números", fontsize=18)
ax.set_xlabel("Valor", fontsize=12)
ax.set_ylabel("Cuadrado del valor", fontsize=12)

# Establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(axis='both', labelsize=12)

plt.show()

