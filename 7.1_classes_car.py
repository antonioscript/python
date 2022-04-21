#Tentativa simples de modelar um carro
smash = "=========================================="
#Criando a classe
class Car ():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year 
		
my_new_car = Car('audi', 'a4', 2016)
print ("O meu carro é: " + my_new_car.make.title())
print ("Seu modelo é: " + my_new_car.model.title())
print ("O ano é: " + str(my_new_car.year))

print (smash)
