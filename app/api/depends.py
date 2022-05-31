from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, model, schema
from app.core import database
from app.core.config import config

"""
Common Depends
"""


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Auth Function
oauth2_password_bearer = OAuth2PasswordBearer(tokenUrl=config.OAUTH2_TOKEN_URL)


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_password_bearer)
) -> model.User:
    try:
        payload = jwt.decode(
            token, config.JWT_SECRET, algorithms=config.JWT_ALGORITHM
        )
        token_data = schema.api_v1.auth.TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=401,
            detail="用户授权信息不正确"  # 此处是用户的Token无法解密
        )
    user = crud.user.get(db, token_data.sub)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="用户授权信息不正确"  # 此处是未能从解密的Token内容中找到所对应的用户身份，即这个口令有可能是伪造的
        )
    return user


def get_current_user_schema(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_password_bearer)
) -> schema.crud.user.UserQuery:
    return schema.crud.user.UserQuery(**jsonable_encoder(get_current_user(db, token)))


def get_super_user(
    user: schema.crud.user.UserQuery = Depends(get_current_user)
):
    if user.permission < 5:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Permission level not enough",
        )
    else:
        return user


def get_super_user_schema(
    user: schema.crud.user.UserQuery = Depends(get_super_user)
) -> schema.crud.user.UserQuery:
    return schema.crud.user.UserQuery(**jsonable_encoder(user))
