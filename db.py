from pymongo import MongoClient

connection_string = 'your connection string'
collection_name = 'b_users'
dummy_record = {
    "id": "himanshu3198",
    "fullname": "himanshu sharma",
    "email": "himanshu31@gmail.com",
    "password": "Damit"
}

client = MongoClient(connection_string)
db = client.Bookmyshow
collection = db[collection_name]
try:
    result = collection.insert_one(dummy_record)
    print("inserted record is", result.inserted_id)
except Exception as e:
    response = {'error occurred': str(e)}
    print(response)
