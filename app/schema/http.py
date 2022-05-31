from pydantic import BaseModel, Field


class HTTP_200_OK(BaseModel):
    status: int = Field(
        200,
        title="状态码"
    )
    msg: str = Field(
        "OK",
        title="提示信息"
    )


class HTTP_301_Moved_Permanently(BaseModel):
    status: int = Field(
        301,
        title="状态码"
    )
    msg: str = Field(
        "Moved Permanently",
        title="提示信息"
    )


class HTTP_302_Found(BaseModel):
    status: int = Field(
        302,
        title="状态码"
    )
    msg: str = Field(
        "Found",
        title="提示信息"
    )


class HTTP_400_Bad_Request(BaseModel):
    status: int = Field(
        400,
        title="状态码"
    )
    msg: str = Field(
        "Bad Request",
        title="提示信息"
    )


class HTTP_401_Unauthorized(BaseModel):
    status: int = Field(
        401,
        title="状态码"
    )
    msg: str = Field(
        "Unauthorized",
        title="提示信息"
    )


class HTTP_403_Forbidden(BaseModel):
    status: int = Field(
        403,
        title="状态码"
    )
    msg: str = Field(
        "Forbidden",
        title="提示信息"
    )


class HTTP_404_Not_Found(BaseModel):
    status: int = Field(
        404,
        title="状态码"
    )
    msg: str = Field(
        "Not Found",
        title="提示信息"
    )


class HTTP_409_Conflict(BaseModel):
    status: int = Field(
        409,
        title="状态码"
    )
    msg: str = Field(
        "Conflict",
        title="提示信息"
    )


class HTTP_422_Unprocessable_Entity(BaseModel):
    status: int = Field(
        422,
        title="状态码"
    )
    msg: str = Field(
        "Unprocessable Entity",
        title="提示信息"
    )


class HTTP_429_Too_Many_Requests(BaseModel):
    status: int = Field(
        429,
        title="状态码"
    )
    msg: str = Field(
        "Too Many Requests",
        title="提示信息"
    )


class HTTP_500_Internal_Server_Error(BaseModel):
    status: int = Field(
        500,
        title="状态码"
    )
    msg: str = Field(
        "Internal Server Error",
        title="提示信息"
    )


class HTTP_501_Not_Implemented(BaseModel):
    status: int = Field(
        501,
        title="状态码"
    )
    msg: str = Field(
        "Not Implemented",
        title="提示信息"
    )


class HTTP_502_Bad_Gateway(BaseModel):
    status: int = Field(
        502,
        title="状态码"
    )
    msg: str = Field(
        "Bad Gateway",
        title="提示信息"
    )


class HTTP_503_Service_Unavailable(BaseModel):
    status: int = Field(
        503,
        title="状态码"
    )
    msg: str = Field(
        "Service Unavailable",
        title="提示信息"
    )


class HTTP_504_Gateway_Timeout(BaseModel):
    status: int = Field(
        504,
        title="状态码"
    )
    msg: str = Field(
        "Gateway Timeout",
        title="提示信息"
    )


class HTTP_507_Insufficient_Storage(BaseModel):
    status: int = Field(
        507,
        title="状态码"
    )
    msg: str = Field(
        "Insufficient Storage",
        title="提示信息"
    )
