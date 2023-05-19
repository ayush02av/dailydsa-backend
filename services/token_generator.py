from schemas.auth import AuthToken
from config import config
import jwt

def generate(user) -> str:
    return jwt.encode(
        AuthToken(**user).dict(),
        config.AUTH_TOKEN_SECRET,
        algorithm = config.AUTH_TOKEN_ALGORITHM
    )