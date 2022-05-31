from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app import crud, schema
from app.api import depends
from app.core import security

router = APIRouter()


# POST /auth/login
@router.post("/login", summary="User Login", responses={
    200: {"model": schema.api_v1.auth.TokenOut},
    401: {"model": schema.http.HTTP_401_Unauthorized},
    422: {"model": schema.http.HTTP_422_Unprocessable_Entity}
})
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(depends.get_db)
):
    user = crud.user.auth_by_username(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(401, 'Incorrect username or password')
    return schema.api_v1.auth.TokenOut(access_token=security.create_access_token(user.id))


# POST /auth/register
@router.post("/register", summary="User Register", responses={
    200: {"model": schema.http.HTTP_200_OK},
    409: {"model": schema.http.HTTP_409_Conflict},
    422: {"model": schema.http.HTTP_422_Unprocessable_Entity}
})
def register(
    user: schema.crud.user.UserCreate,
    db=Depends(depends.get_db)
):
    # Here restricts the username must be the same as the phone number
    if crud.user.get_by_username(db, user.username):
        raise HTTPException(409, 'The specified user already exists')
    crud.user.create(db, user)

    return schema.http.HTTP_200_OK()


# GET /auth/renew_token
@router.get("/renew_token", summary="Refresh token", responses={
    200: {"model": schema.api_v1.auth.TokenOut},
    401: {"model": schema.http.HTTP_401_Unauthorized}
})
def renew_token(
    user: schema.crud.user.UserQuery = Depends(depends.get_current_user_schema)
):
    return schema.api_v1.auth.TokenOut(access_token=security.create_access_token(user.id))


# POST /auth/change_password
@router.post("/change_password", summary="Change Password", responses={
    200: {"model": schema.http.HTTP_200_OK},
    400: {"model": schema.http.HTTP_400_Bad_Request},
    401: {"model": schema.http.HTTP_401_Unauthorized},
    422: {"model": schema.http.HTTP_422_Unprocessable_Entity}
})
def change_password(
    data: schema.api_v1.auth.ChangePWIn,
    user: schema.crud.user.UserQuery = Depends(depends.get_current_user_schema),
    db=Depends(depends.get_db)
):
    user_data = crud.user.auth_by_id(db, user.id, data.password_old)
    if not user_data:
        raise HTTPException(400, 'Incorrect username or password')
    crud.user.update(db, db_obj=user_data, obj_in=schema.crud.user.UserUpdate(password=data.password))
    return schema.http.HTTP_200_OK()


# POST /auth/unregister
@router.post("/unregister", summary="User Unregister", responses={
    200: {"model": schema.http.HTTP_200_OK},
    400: {"model": schema.http.HTTP_400_Bad_Request},
    401: {"model": schema.http.HTTP_401_Unauthorized},
    422: {"model": schema.http.HTTP_422_Unprocessable_Entity}
})
def unregister(
    confirm: schema.api_v1.auth.UnregisterIn,
    user: schema.crud.user.UserQuery = Depends(depends.get_current_user_schema),
    db=Depends(depends.get_db)
):
    user_data = crud.user.auth_by_id(db, user.id, confirm.password)
    if (not user_data) or (user.id != user_data.id):
        raise HTTPException(400, 'Incorrect username or password')
    crud.user.delete(db, user_data.id)
    return schema.http.HTTP_200_OK()
