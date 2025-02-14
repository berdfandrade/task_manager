import bcrypt


def hash_password(password: str) -> str:
    """Gera um hash seguro para a senha fornecida."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()  # Convertendo para string para armazenamento


def verify_password(password: str, hashed_password: str) -> bool:
    """Verifica se a senha corresponde ao hash armazenado."""
    return bcrypt.checkpw(
        password.encode(),
        (
            hashed_password.encode()
            if isinstance(hashed_password, str)
            else hashed_password
        ),
    )
