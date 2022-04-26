#Remodelagem (reshape)
smash = "============================"

#Remodelando 1 dimensão em 2 dimensão
#O resultado será 4 matrizes (linear) com 3 elementos cada uma
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newwarr = arr.reshape(4,3) #4matrizes e 3 elementos cada uma
print(newwarr)

print(smash)

import numpy as np
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newwarr2 = arr.reshape(2, 3, 2)#2 matrizes, com 3 linhas e 2 elementos cada uma
print(newwarr2)

