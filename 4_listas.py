#******CRIANDO LISTAS******

lista = ["queijo", "mortadela", "batata", "leite"];
print (lista);

#Para buscar um item, digitar o índice que começa em 0

print (lista[0]);
print (lista[0].title());

#Excluir um item

del lista[2];
print (lista);

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



