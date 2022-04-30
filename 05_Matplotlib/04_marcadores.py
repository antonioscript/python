#Marcadores
#Marcando um círculo em cada ponto
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = "o")
plt.show()

#Lista de Marcadores
# o - Círculo
# * - Estrela
# . - Ponto
# , - Pixel
# x - X
# + - Plus
# s - Square
# D - Diamante
# p - Pentágono
# h - Hexágono
# v - Triângulo
#...

#Cores e Estilos da Linha
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, "o:r") #Significa Círculos e Vermelho
plt.show()

#r - Red
#g - Green
#b - Blue
#c - Cyan
#m - Magenta
#y - yellow
#k - Black
#w - White

#Tamanho dos marcadores
import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = "o", ms = 20)
plt.show()

#Obs: Existem diversos marcadores, cores, estilos, etc. 
#Para saber mais, acessar o manual da W3School
#https://www.w3schools.com/python/matplotlib_markers.asp

