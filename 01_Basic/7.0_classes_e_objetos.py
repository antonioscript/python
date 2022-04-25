#***Classes e Objetos***

#TODA CLASSE TEM ATRIBUTOS E MÉTODOS

#Classes = Atributos, Molde, Esqueleto, São propriedades (Cor, tamanho, etc)
#Métodos = Funções (O que aquilo faz)

#Molde - > Marca, Memória Ram, Placa de Vídeo
class Computador: #Atributos
	def __init__(self, marca, memoria, placa):
		self.marca = marca
		self.memoria = memoria
		self.placa = placa

#Funcionalidades computador (métodos, funções):
#Ligar, Desligar, Exibir Configurações, etc
	
	def Ligar(self): #Métodos
		print("Estou ligando")
	
	def Desligar(self): #Métodos
		print("Estou desligando")
	
	def Exibir(self): #Métodos
		print(self.marca, self.memoria, self.placa)


computador1 = Computador("Asus", "8gb", "Nvida")
computador1.Ligar()
computador1.Desligar()
computador1.Exibir()

#computador2 = Computador("IOS", "16gb", "Gtx")
#computador3 = Computador("Compaq", "4gb", "Comum")

#print(computador1.marca, computador1.memoria, computador1.placa)
#print(computador2.marca, computador2.memoria, computador2.placa)
#print(computador3.marca, computador3.memoria, computador3.placa)


