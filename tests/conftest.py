import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
import os

# Pega a URL do banco de testes
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")