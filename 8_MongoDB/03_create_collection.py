import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wbanco"]

mycol = mydb["customers"]
print(mydb.list_collection_names())
