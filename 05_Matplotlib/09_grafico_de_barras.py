#Criando Gráfico de Barras
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y) #Perceba que ao invés do comum "plot", utilizamos "bar"
plt.show()

#Se for barra orizontal, utiliza 'plt.barh'

