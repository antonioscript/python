#***** INSTRUÇÃO IF ELSE*******	
	#if condição:
		#print ();
	#elif:
		#print ();
	#else: 
		#print ();
		
#***** LOOP WHILE*******
	#while condição:
		#Print ();

barra = "======================================"

#Descobrindo se pode votar
age = 19
if age >= 16:
	print ("Tudo tranquilo, já pode votar");
else:
	print ("Espere mais um pouco");	


print (barra)

#Descobrindo valor a pagar
idade = 45
if idade < 4:
	print ("Sua entrada é gratuita")
elif idade < 18:
	print ("Você paga R$ 5, 00")
elif idade >= 65: #Pode Usar quantos Elif quiser
	print ("Você paga R$ 10, 00")
else:
	print ("Você paga 20, 00")

print (barra);




#Colocando a palavra bmw em maiúscula
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print (car.upper())
	else:
		print (car.title())

print (barra)		
#loop while

spam = 0
if spam < 5:
	print ("Oi, Mundo");
	spam = spam + 1;

spam2 = 0
while spam2 < 5:
	print ("Oi, Mundo");
	spam2 = spam2 + 1; #Se não fizer isso cai em loop 
print (barra)
