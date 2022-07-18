import pymongo

client = pymongo.MongoClient("mongodb+srv://Mukesh:rt32jRVbOtTsTsfx@cluster0.iahh6bv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d1={
    "name":"mukesh",
    "email":"sizal@gmail.com",
    "surname":"kumar"

}

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)

db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)
db2=client['mongotest2']
coll=db2['test']
coll.insert_one(d1)
