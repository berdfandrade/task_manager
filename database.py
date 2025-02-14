import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carregar variáveis do .env
load_dotenv()

# Pegando a variável correta
DATABASE_URL = os.getenv("DATABASE_URL")

# Criando o engine
engine = create_engine(DATABASE_URL)

# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()


# Função para obter a sessão do banco (get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db  # Retorna a sessão para ser usada na requisição
    finally:
        db.close()  # Fecha a sessão depois do uso
