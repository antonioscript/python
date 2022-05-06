#Classificar por ordem crescente
import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost", 
	user = "root", 
	password = "1915691", 
	database = "mydatabase"
)

mycursor = mydb.cursor()

#Ordenar os nomes em ordem alfabética (crescente)
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


print("-" * 50)

#Ordem Descrescente
sql = "SELECT * FROM customers ORDER BY name DESC" #Adiciona o 'DESC'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
