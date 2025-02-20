import pytest
from service.user_service import UserService
from schemas.UserSchema import UserCreate
from tests.utils.reset_database import clear_table

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """Limpa a tabela 'users antes de cada teste automaticamente"""
    clear_table('users')
    yield 
    clear_table('users')
    
def test_create_user(db):
    """Testa se o usuário é criado corretamente no PostgreSQL."""
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        password="testpassword",
        bio="Bio de teste",
    )

    # Chama a função para criar o usuário e passa a sessão db
    user = UserService.create_user(db, user_data)

    # Assegura que o usuário foi criado
    assert user.id is not None  # Garante que foi gerado um ID
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.bio == "Bio de teste"


def test_create_user_with_same_email(db):
    """Teste se é possível criar um usuário com o mesmo email."""

    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        password="testpassword",
        bio="Bio de teste",
    )
    
    # Chama a função para criar o usuário e passa a sessão db
    UserService.create_user(db, user_data)
    
    # Tenta criar outro usuário com o mesmo e-mail, mas nome de usuário diferente
    duplicate_user_data = UserCreate(
        username="testuser2",
        email="test@example.com",  # Mesmo e-mail do primeiro usuário
        password="testpassword",
        bio="Outra bio",
    )
    
    # Verifica se um erro é lançado ao tentar criar o usuário duplicado 
    with pytest.raises(ValueError) as exc_info:
        UserService.create_user(db, duplicate_user_data)
        
    assert str(exc_info.value) == f"Email '{user_data.email}' already exists."


