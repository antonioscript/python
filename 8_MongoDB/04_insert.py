import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wbanco"]
mycol = mydb["customers"]

mydict = { "name": "Maria", "address": "Magdália" }

x = mycol.insert_one(mydict)
print("Registro Inserido")
