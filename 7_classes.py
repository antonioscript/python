#Programação Orientada a Objetos
smash = "========================================"
#Tentativa simples de modelar um cachorro
class Dog(): #Primeira letra em maiúscula (opcional)
	def __init__(self, name, age): #Inicializa os atributos name e age
		self.name = name #variáveis
		self.age = age   #variáveis

#sentar e rolar são métodos
#name e age, características
	def sentar(self): #Simula um cachorro sentando em resposta a um comando
		print (self.name.title() + " Agora está sentado")

	def rolar(self): #Simula um cachorro rolando em respostasa um comando
		print (self.name.title() + ", Rolar!")

#Criando uma instância
my_dog = Dog('Bob', 6)
#Acessando Atributos
print ("O nome do meu cachorro é:",my_dog.name.title())
print ("Meu cachorro tem:",str(my_dog.age), "anos de idade")

#Acessando Métodos
my_dog.sentar()
my_dog.rolar()

print (smash)

#Criando outra instância
my_dog = Dog('Bob', 6)
your_dog = Dog('Bethoven', 8)
print ("O nome do meu cachorro é: " + my_dog.name.title())
print ("Meu cachorro tem: " + str(my_dog.age) + " anos de idade")
my_dog.sentar()

print (smash)

print ("O nome do seu cachorro é: " + your_dog.name.title())
print ("seu cachorro tem: " + str(your_dog.age) + " anos de idade")
your_dog.rolar()
