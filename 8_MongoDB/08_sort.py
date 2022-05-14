import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wbanco"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

print("-" * 90)

#Obs: sort("name", 1) #ascending
#	  sort("name", -1) #descending


mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
