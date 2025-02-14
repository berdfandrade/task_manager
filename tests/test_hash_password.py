import pytest
from utils.password import hash_password, verify_password


def test_hash_password():
    """Testa se a senha é corretamente hasheada."""
    password = "minha_senha_segura"
    hashed = hash_password(password)
    assert isinstance(hashed, str)
    assert hashed != password  # O hash nunca deve ser igual à senha original


def test_verify_password():
    """Testa se a senha fornecida corresponde ao hash armazenado."""
    password = "minha_senha_segura"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("senha_errada", hashed) is False
