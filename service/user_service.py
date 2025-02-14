from sqlalchemy.orm import Session
from models.user import User
from schemas.UserSchema import UserCreate
from utils.password import hash_password
from sqlalchemy.exc import IntegrityError

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
        # Verifica se o username ou o e-mail já estão em uso
        existing_user = UserService.get_user_by_email_or_username(
            db, user_data.email, user_data.username
        )
        
        if existing_user:
            if existing_user.username == user_data.username:
                raise ValueError(f"Username '{user_data.username}' already exists.")
            if existing_user.email == user_data.email:
                raise ValueError(f"Email '{user_data.email}' already exists.")

        # Criptografa a senha
        hashed_password = hash_password(user_data.password)
        
        # Cria o novo usuário
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            bio=user_data.bio,
        )

        # Adiciona o usuário no banco de dados
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
