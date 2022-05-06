#Criando tabela
import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1915691",
	database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE clientes (name VARCHAR(255), andress VARCHAR (255))")


