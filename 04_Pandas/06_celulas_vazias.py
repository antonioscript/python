#Limpando células vazias, com a remoção de linhas
#'dropna'
import pandas as pd
df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string())

#Obs: Ele não apaga o arquivo original, retorna apenas um novo dataframe
#Para mudar o arquivo orginal, use o argumento- > 'inplace = True'

import pandas as pd
df2 = pd.read_csv("data.csv")
df2.dropna(inplace = True)
print(df2.to_string())
