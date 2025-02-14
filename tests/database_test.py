import os 
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Importar a configuração do banco de dados
from database import DATABASE_URL, SessionLocal, engine

def test_database_url_loaded():
    """Testa se a variável DATABASE_URL foi carregada corretamente."""
    assert DATABASE_URL is not None, "DATABASE_URL não foi carregado corretamente"
    assert isinstance(DATABASE_URL, str), "DATABASE_URL deve ser uma string"
    assert DATABASE_URL.startswith("postgresql"), "DATABASE_URL deve ser uma URL PostgreSQL válida"

def test_engine_creation():
    """Testa se a engine do SQLAlchemy foi criada corretamente."""
    assert engine is not None, "Engine não foi inicializada"
    assert isinstance(engine, create_engine("sqlite://").__class__), "Engine deve ser uma instância de create_engine"

def test_session_creation():
    """Testa se a sessão do banco de dados pode ser criada corretamente."""
    session = SessionLocal()
    assert session is not None, "Sessão do banco de dados não foi criada"
    session.close()

if __name__ == "__main__":
    pytest.main()
