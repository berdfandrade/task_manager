from sqlalchemy.orm import Session
from models.user import User
from schemas.UserSchema import UserCreate, UserUpdate
from utils.password import hash_password
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

    @staticmethod
    def get_users(db: Session):
        """Retorna todos os usuários cadastradaos no bando de dados"""
        return db.query(User).all()

    @staticmethod
    def update_user(db: Session, user_id: str, user_data: UserUpdate):
        """Atualiza os dados de um usuário"""
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User not found")

        # Verifica se o novo e-mail ou username já estão em uso por outro usuário
        if user_data.email or user_data.username:
            existing_user = (
                db.query(User)
                .filter(
                    (User.email == user_data.email)
                    | (User.username == user_data.username),
                    User.id != user_id,
                )
                .first()
            )

        # Atualiza os campos permitidos
        if user_data.username:
            user.username = user_data.username
        if user_data.email:
            user.email = user_data.email
        if user_data.bio:
            user.bio = user_data.bio
        if user_data.password:
            user.password = hash_password(user_data.password)

        # Salva as alterações no banco de dados
        db.commit()
        db.refresh(user)
        
        return user