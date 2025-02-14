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
    transaction = session.begin()  # Inicia uma transação

    # Obtém o nome de todas as tabelas no banco de dados
    inspector = inspect(session.bind)
    tables = inspector.get_table_names()

    # Limpa todas as tabelas (sem deletá-las)
    for table in tables:
        session.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE;")
        print(f"Table '{table}' cleaned.")  # Imprime qual tabela foi limpa

    session.commit()  # Aplica as alterações no banco
    yield session  # Roda o teste com essa sessão
    transaction.rollback()  # Reverte tudo o que foi feito no teste
    session.close()

# TODO : RESOLVER ISSO DEPOIS 