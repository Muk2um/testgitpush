import pymongo

client = pymongo.MongoClient("mongodb+srv://Mukesh:rt32jRVbOtTsTsfx@cluster0.iahh6bv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name":"mukesh",
    "email":"sizal@gmail.com",
    "surname":"kumar"

}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
