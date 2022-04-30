#Gráfico de Pizzas
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Maças", "Bananas", "Morangos", "Peras"]

plt.pie(y, labels = mylabels)
plt.show()
