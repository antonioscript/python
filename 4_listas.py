#******CRIANDO LISTAS******

lista = ["queijo", "mortadela", "batata", "leite"];
print (lista);

#Para buscar um item, digitar o índice que começa em 0

print (lista[0]);
print (lista[0].title());

#Excluir um item

del lista[2];
print (lista);

smash = "======================================="
#Criando uma lista

mylist = ["mortadela", "queijo", "ovo", "frango", "salsicha"]

#Mostrando a lista na tela
print(mylist)

print(smash)

#Acessando itens
print(mylist[2])
print(mylist[2:4])
print(mylist[2].title()) #Acessando e colocando a 1º letra maiúscula

print (smash)

#Verificando se um item existe
if "queijo" in mylist:
	print("Sim! Queijo está na lista")
	
print (smash)

#Mudando itens de uma lista
mylist[0] = "presunto" #trocando mortadela por presunto
print(mylist)

print(smash)

#Adicionando itens em uma lista 'append()'
mylist.append("laranja")
print(mylist)

print(smash)

#Adcionando itens no índice ordenado 'insert()'
mylist.insert(3, "abacate") #Adicionando abacate no índice 3
print (mylist)

print(smash)

#deletando item de uma lista
del mylist[2]
print (mylist)

print(smash)

#mostrando numero de itens da lista
print(len(mylist))

print(smash)

#Ordenando a lista em ordem alfabética com a função Sort()

car = ["yamaha", "susuki", "toyota", "chevrolet"];
car.sort();
print (car);


#Percorrendo uma lista inteira com um laço

magicos = ['Alice', 'David', 'Zatanna', 'Hollic', 'Kirk'];
for magico in magicos: #Observe o uso do "dois pontos"
	print (magico); #Observe a indentação

#Criando Listas Numéricas (Função range () )

for valor in range(1,6):
	print (valor)

#Série de Números

numbers = list(range(1,6))
print (numbers)



