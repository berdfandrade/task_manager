import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega o .env
load_dotenv()

# Cria a conexão com o banco de testes
DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def clear_table(TABLE : str):
    """Remove todos os registros da tabela users sem apagar outras tabelas."""
    with engine.connect() as conn:
        conn.execute(text(f'DELETE FROM {TABLE};')) 
        conn.commit()

    print(f"Tabela {TABLE} limpa com sucesso!")
