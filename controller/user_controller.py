from fastapi import HTTPException
from sqlalchemy.orm import Session
from service.user_service import UserService
from schemas.UserSchema import UserCreate


class UserController:
    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        """Controla a criação do usuário, validando e chamando o service."""
        if UserService.get_user_by_email_or_username(
            db, user_data.email, user_data.username
        ):
            raise HTTPException(
                status_code=400, detail="Email ou username já estão em uso"
            )

        return UserService.create_user(db, user_data)

    @staticmethod
    def get_all_users(db : Session):
        return UserService.get_users()