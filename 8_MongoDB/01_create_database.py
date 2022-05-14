import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["wbanco"] #Aqui ele criou o banco de dados
