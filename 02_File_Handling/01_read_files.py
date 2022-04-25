#File Handling
#Função 'open("nome_arquivo.txt")
#r = Read
#Função 'read()' -> ler arquivo
smash = "========================"

#Lendo o arquivo
arquivo = open("demofile.txt", "r")
print(arquivo.read())

print(smash)

#Lendo partes de um arquivo
arquivo2 = open("demofile.txt", "r")
print(arquivo2.read(5)) #Retorna os 5 primeiros caracteres do arquivo

print(smash)

#Lendo Linhas
arquivo3 = open("demofile.txt", "r")
print(arquivo3.readline()) #Retorna a 1º Linha do arquiv

print(smash)

#Fechando arquivos (Boa prática apenas)
arquivo4 = open("demofile.txt", "r")
print(arquivo4.readline())
arquivo4.close()


