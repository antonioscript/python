#Dicionário sempre inicia por "{"
#Par Chave-Valor
alien_0 = {'color': 'green'} #isso é um dicionário
#Color é a chave e o valor é green
print (alien_0['color'])

barra = '======================'
print (barra)

alien_1={'color': 'green', 'points': 5} #Isso é um dicionário
print (alien_1['points']) #Acessando um valor do dicionário (deverá retornar '5')


print (barra)

#Adicionando mais informações a um dicionário
#vamos adicionar por exemplo 'poder' e 'habilidade'

alien_1['power'] = 200
alien_1['habilidade'] = 45
print(alien_1) #Quando exibir mostrará os novos valores

print (barra)

#Começando um dicionário vazio
alien_3 = {}
alien_3['color'] = 'green'
alien_3['points'] = 5
print (alien_3)

print (barra)

#Deletando pares chave-valor

del alien_3['points']
print (alien_3)

#Um dicionário pode ser assim escrito também
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print(barra)

##########################################################
#Novo Dicionário
dicio = {
	"marvel":"vingadores",
	"dc":"liga da justiça", 
	"fox":"x-men",
	"warner":"harry potter",
}
print(dicio)

#Acessado itens do dicionário
print(dicio["fox"])

print(barra)
