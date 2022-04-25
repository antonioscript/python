smash = "=========================================="
#Lendo um arquivo inteiro
with open('py_digits.txt') as file_object:
	conteudo = file_object.read()
	print (conteudo)

print (smash)

#Lendo dados linha a linha
filename = 'py_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print (line)

print (smash)

#Criando uma lista de linhas de um arquivo

