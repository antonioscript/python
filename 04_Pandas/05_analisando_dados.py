smash="========================"
#Método 'head()' retorna o cabeçalho e um número especificado de linhas
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head(10)) #Se não especificar, ele retorna os 5 primeiros

print(smash)

#Método 'tail' retorna o cabeçalho e as últimas linhas
print(df.tail())

print(smash)

#Método 'info' retorna informações sobre os dados
print(df.info())
