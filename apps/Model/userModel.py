from pydantic import BaseModel, EmailStr


class userAddModel(BaseModel):
    id: str
    fullname: str
    email: EmailStr
    password: str
