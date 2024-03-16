from typing import List

from pymongo import MongoClient

from apps.Model.userModel import userAddModel

db_url = 'your url'
user_db_name = 'Bookmyshow'
user_collection_name = 'b_users'


class userRepository:
    def __init__(self):
        self.client = MongoClient(db_url)
        self.db = self.client[user_db_name]
        self.collection = self.db[user_collection_name]

    def add_user(self, user: userAddModel) -> str:
        result = self.collection.insert_one(user.dict())
        return str(result.inserted_id)

    def get_all_users(self) -> List[userAddModel]:
        return [userAddModel(**user) for user in self.collection.find()]
