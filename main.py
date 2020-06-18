import pymongo
import json

# edit by your server
myclient = pymongo.MongoClient("mongodb://192.168.56.102:27017/")

database_name = "testdb2"

# check existance db
dblist = myclient.list_database_names()
if database_name in dblist:
    # set db
    mydb = myclient[database_name]
    mycol = mydb['transaction']
else:
    mydb = myclient[database_name]
    mydb.create_collection(name="transaction")
    mycol = mydb['transaction']


def main():
    mydb.create_collection(name="user")
    insert_transaction = [{'name': 'john', 'values': 123},
                          {'name': 'wick', 'values': 12}]
    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]
    mycol.insert_many(documents=mylist)

    mycol.delete_many({"name": "john"})

    mycol.update({"name": "wick"}, {"$set": {"comments": [
                 "This is comment", "This is comment2"]}})

    for i in mycol.find().sort("name"):
        print(i)


if __name__ == "__main__":
    main()
