from typing import List

from apps.Model.userModel import userAddModel
from apps.Repository.userRepository import userRepository


def get_all_user():
    return "this is users"


class userService:
    def __init__(self):
        self.user_repo = userRepository()

    def add_user(self, user: userAddModel) -> str:
        # user = userAddModel(**use)
        user_info = self.user_repo.add_user(user)
        return user_info

    def get_all_users(self) -> List[userAddModel]:
        return self.user_repo.get_all_users()
