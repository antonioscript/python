#Estilos de linha
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = "dotted")
plt.show()

# - - Solid
#: - Dotted
#-. - Dashdot

#Cor da linha
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = "r") #Pode ser hexadecimal também
plt.show()

#Largura da linha
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = "20.5") 
plt.show()


#Multiplas linhas
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()

#Acessar para mais informações:
#https://www.w3schools.com/python/matplotlib_line.asp







