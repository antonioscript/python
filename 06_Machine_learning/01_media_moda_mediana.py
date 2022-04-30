import numpy as np

#Calculando a Média
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

#Calculando a Mediana
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
y = np.median(speed)
print(y)

#Calculando a Moda
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
