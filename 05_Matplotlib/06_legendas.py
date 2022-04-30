#Legendas
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Whatch Data") #Título do Gráfico
plt.xlabel("Average Pulse") #Legenda x
plt.ylabel("Calorie Burnage") #Legenda y

#Adicionando grids #quadriculado
plt.grid()

plt.show()



