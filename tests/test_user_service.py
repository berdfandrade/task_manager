import pytest
from service.user_service import UserService
from schemas.UserSchema import UserCreate
from tests.utils.reset_database import clear_table

def test_create_user(db):
    
    """Testa se o usuário é criado corretamente no PostgreSQL."""
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        password="testpassword",
        bio="Bio de teste"
    )

    # Chama a função para criar o usuário e passa a sessão db
    user = UserService.create_user(db, user_data)

    # Assegura que o usuário foi criado
    assert user.id is not None  # Garante que foi gerado um ID
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.bio == "Bio de teste"
    
    # Limpa a tabela users
    clear_table('users')

