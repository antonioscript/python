#Carregando o arquivo dentro do DataFrame
smash = "======================="

import pandas as pd
df = pd.read_csv("data.csv")
print(df.to_string())
#Obs: Se não colocar 'to_string()', o Pandas só retorna os 5 primeiros
#E os 5 últimos
import pandas as pd

print(smash)

#Aumentando o número de linhas para imprmir o dataframe inteiro
import pandas as pd
pd.options.display.max_rows = 9999
df2 = pd.read_csv('data.csv')
print(df2) 

