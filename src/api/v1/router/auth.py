from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import JSONResponse

from src.api.schemas.user_schemas import UserCreate, UserLogin
from src.domain.usecases.user.create import CreateUserUsecase
from src.domain.usecases.user.check import CheckUserUsecase

from src.services.auth import PasswordService, JWTService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login",
             status_code=status.HTTP_200_OK)
async def login(user: UserLogin, cuu: Annotated[CheckUserUsecase, Depends(CheckUserUsecase)]):
    try:
        logged_user = await cuu.check_user(user)
        try:
            token = JWTService.sign_jwt(logged_user.username)
            response = JSONResponse(status_code=HTTPStatus.CREATED, content=logged_user.model_dump())
            response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
            return response
        except Exception as ex:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))


@router.post("/signin",
             status_code=status.HTTP_201_CREATED)
async def sign_in(user: UserCreate, cuu: Annotated[CreateUserUsecase, Depends(CreateUserUsecase)]):
    user_new_password = PasswordService.create_password(user.password)
    user.password = user_new_password
    try:
        await cuu.create_user(user)
    except Exception as ex:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))
    return JSONResponse(status_code=HTTPStatus.CREATED, content={"logged": "logged"})
