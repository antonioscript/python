#Escrevendo e Criando arquivos
#'a' - Append, anexar algo ao final do arquivo (preserva o arquivo)
#'w' - Write, substitui (apaga) o conteúdo
smash = "========================="

#Anexando texto
arquivo = open("demofile2.txt", "a")
arquivo.write("Agora o arquivo tem mais conteúdo")
arquivo.close()

#open and read the file after the appending:
arquivo = open("demofile2.txt", "r")
print(arquivo.read())

print(smash)

#Obs: Vale lembrar que a cada execução do programa ele escreve o texto

#Escrevendo
arquivo3 = open("demofile3.txt", "w")
arquivo3.write("Opa, acho que deletei todo o conteúdo!")
arquivo3.close()

arquivo3 = open("demofile3.txt", "r")
print(arquivo3.read())

