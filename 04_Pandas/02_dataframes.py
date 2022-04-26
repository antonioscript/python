#Criando DataFrame
smash = "========================"

import pandas as pd
data = {
	"calories":[420,380,390],
	"duration":[50,40,45]
}
df = pd.DataFrame(data)
print(df)

print(smash)

#Localizando -> 'loc'
print(df.loc[0])

print(smash)

#Renomeando os índices
import pandas as pd
data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df2 = pd.DataFrame(data2, index = ["day1", "day2", "day3"])
print(df2) 

print(smash)

#Localizando o item
print(df2.loc["day2"])
