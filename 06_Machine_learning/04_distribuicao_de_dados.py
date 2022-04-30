#Muitos dados
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 250)
#O comando está dizendo: 250 números entre 0 e 5
print(x)
#Podemos representar em um histograma
plt.hist(x, 5) #5 barras
plt.show()


#Big dados
x = np.random.uniform(0.0, 5.0, 100000) #Cem Mil

plt.hist(x, 100) #Cem Barras
plt.show()
