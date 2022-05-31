from typing import Optional

from pydantic import BaseModel, Field


# Model Base Schema
class UserBasic(BaseModel):
    nickname: Optional[str] = Field(None, title="用户昵称", max_length=32)


# Create Schema
class UserCreate(UserBasic):
    username: str = Field(..., title="登录用户名", max_length=32)
    password: str = Field(..., title="登录密码", min_length=1, max_length=32)


# Update Schema
class UserUpdate(UserBasic):
    username: Optional[str] = Field(None, title="登录用户名", max_length=32)
    password: Optional[str] = Field(None, title="登录密码", max_length=32)
    permission: Optional[int] = Field(None, title="用户权限等级")


# Select Schema
class UserQuery(BaseModel):
    id: Optional[str] = ""
    nickname: Optional[str] = ""
    username: Optional[str] = ""
    password: Optional[str] = ""
    permission: Optional[int] = 1

    class Config:
        orm_mode = True
