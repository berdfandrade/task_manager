from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Cria a conexão com o banco de testes
DATABASE_URL = "postgresql://bernardo:123@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def reset_database():
    """Remove todas as tabelas do banco de testes e recria o esquema."""
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))  # Remove todas as tabelas
        conn.execute(text("CREATE SCHEMA public;"))  # Recria o esquema padrão
        conn.execute(text("GRANT ALL ON SCHEMA public TO postgres;"))
        conn.execute(text("GRANT ALL ON SCHEMA public TO public;"))
        conn.commit()

    print("Banco de testes resetado com sucesso!")

if __name__ == "__main__":
    reset_database()