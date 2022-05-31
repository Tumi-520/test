from typing import Optional
from pydantic import Field, BaseModel


# OTHER / User Authorization
class TokenPayload(BaseModel):
    sub: Optional[str] = Field(None, title="令牌内容")


# POST /auth/login OUTPUT
# POST /auth/renew_token OUTPUT
class TokenOut(BaseModel):
    status: int = Field(200, title="状态码")
    msg: str = Field("OK", title="提示信息")
    access_token: str = Field(..., title="令牌内容")
    token_type: str = Field("bearer", title="令牌类型")


# POST /auth/unregister INPUT
class UnregisterIn(BaseModel):
    password: str = Field(..., title="登录密码", min_length=1, max_length=32)


# POST /auth/change_password INPUT
class ChangePWIn(BaseModel):
    password: str = Field(..., title="原密码", min_length=1, max_length=32)
    password_old: str = Field(..., title="新密码", min_length=1, max_length=32)
