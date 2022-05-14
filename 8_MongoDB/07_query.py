#Encontrar informações completas passando parte da informação

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wbanco"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
