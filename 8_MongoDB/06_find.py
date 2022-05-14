import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wbanco"]
mycol = mydb["customers"]

x = mycol.find_one() #Retorna sempre o primeiro

print(x)

#Para Retornar os outros, basta fazer um loop
for x in mycol.find():
	print(x)
 
