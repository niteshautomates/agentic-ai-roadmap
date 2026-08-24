from pydantic import BaseModel, EmailStr

class UserProfile(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    is_active: bool = True


data = {
    "user_id": "123",
    "username": "johndoe",
    "email": "john@example.com"
}


user = UserProfile(**data)  # This will validate the data and create a UserProfile instance
print(user.user_id ,  type(user.user_id))
