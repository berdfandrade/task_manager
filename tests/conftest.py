import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from database import Base
import os

# Pega a URL do banco de testes
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

# Cria o engine e a sessão para testes
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Cria uma sessão de teste, limpa todas as tabelas e reverte as mudanças após o teste"""
    session = TestingSessionLocal()
    yield session
    session.close()
