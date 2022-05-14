import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
if "wbanco" in dblist:
  print("The database exists.")
else:
	print("Database não existe")
