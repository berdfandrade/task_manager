from fastapi import APIRouter, Depends
from controller.user_controller import UserController
from sqlalchemy.orm import Session
from database import get_db
from schemas.UserSchema import UserCreate, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return UserController.create_user(user_data, db)

@router.get("/", status_code=200)
def check_health():
    return {"message" : "Hello, World!"}