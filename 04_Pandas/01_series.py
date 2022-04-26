#Começando com pandas
smash = "========================="

import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

print(smash)

#Retornando o primeiro valor da Série
print(myvar[0])

print(smash)

#Renomenando os índices
import pandas as pd
b = [1, 7, 2]
myvar2 = pd.Series(b, index = ["x", "y", "z"])
print(myvar2)

print(smash)

#Retornando valor específico
print(myvar2["y"])

print(smash)

#Criando uma série a partir de um dicionário
import pandas as pd
calories = {"day1":420, "day2":390, "day3":320}
myvar3 = pd.Series(calories)
print(myvar3)
