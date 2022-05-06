import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1915691",
  database="mydatabase"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
