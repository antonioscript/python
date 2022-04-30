#Distribuição normal de dados
#Significa que todos os valores estão concentrados em torno de 
#um determinado valor

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 100000) #Valor médio = 5 e Desvio Pad = 1

plt.hist(x, 100)
plt.show()

#Gráfico de dispersão

x1 = np.random.normal(5.0, 1.0, 1000)
y1 = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x1, y1)
plt.show()
