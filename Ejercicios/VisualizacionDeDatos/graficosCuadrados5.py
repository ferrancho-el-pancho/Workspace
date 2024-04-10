import matplotlib.pyplot as plt

valores = [num for num in range(1, 5001)]
cubos = [num**3 for num in valores]
fig, ax = plt.subplots()
ax.plot(valores, cubos)


ax.set_title("Cubos de los números", fontsize=18)
ax.set_xlabel("Valor", fontsize=12)
ax.set_ylabel("Cubo del valor", fontsize=12)



plt.show()