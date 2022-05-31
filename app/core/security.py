from base64 import b64encode, b64decode
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from .config import config


# JWT Token Create
def create_access_token(subject: str, expire_time: timedelta = None) -> str:
    if expire_time:
        expire = datetime.utcnow() + expire_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


# deal with bcrypt password (require passlib[bcrypt])
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return bcrypt_context.hash(password)
