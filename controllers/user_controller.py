from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import UserService

router = APIRouter()

@router.post("/users/")
def create_user(user: User):
    return UserService.add_user(user)

@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = UserService.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/")
def read_users():
    users = UserService.get_userall()
    if users is None:
        raise HTTPException(status_code=404, detail="No users found")
    return users