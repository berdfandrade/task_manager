from sqlalchemy.orm import Session
from models.user import User
from schemas.UserSchema import UserCreate
from utils.password import hash_password


class UserService:
    @staticmethod
    def get_user_by_email_or_username(db: Session, email: str, username: str):
        """Verifica se já existe um usuário com esse e-mail ou username."""
        return (
            db.query(User)
            .filter((User.email == email) | (User.username == username))
            .first()
        )

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        hashed_password = hash_password(user_data.password)
        
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            bio=user_data.bio,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
        
