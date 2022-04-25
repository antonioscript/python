#Criando arrays
#'ndarray"
smash = "======================="

#Criando Arry
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(smash)

#0-D Array 
import numpy as np
arr = np.array(42)
print(arr)

print(smash)

#1-D Array
import numpy as np
arr = np.array([1,2,3])
print (arr)

print(smash)

#2-D Array
import numpy as np
arr = np.array([[1,2,3], [4,5,6]])
print (arr)

print(smash)

#3-D Array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

print(smash)

#Verificando o número de dimensões de um array
#"ndim" -> Número de dimensão
#Exemplo

print(arr.ndim)
