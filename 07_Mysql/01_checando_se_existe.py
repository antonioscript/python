#Checando se existe

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1915691" #ou
  #database = "mydatabase" -> Se não apresentar erro, então existe
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

#Isso mostra todos os bancos de dados existentes
