#Múltiplos Gráficos nas mesma imagem - 'subplt()'
import matplotlib.pyplot as plt
import numpy as np

#plot1:
x = np.array([0, 1, 2, 3])
y = np.array ([3, 8, 1, 10])

plt.subplot(1, 2, 1) #1 linha, 2 colunas e 1º plot
plt.plot(x,y)

#plot2:
x = np.array([0, 1, 2, 3])
y = np.array ([10, 20, 30, 40])

plt.subplot(1, 2, 2) #1linha, 2 colunas e 2º plot
plt.plot(x,y)

plt.show()

#Dá pra adicionar inúmeros gráficos na mesma página



