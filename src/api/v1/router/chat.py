from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import JSONResponse
from starlette.websockets import WebSocket

from src.api.dependencies.auth import get_current_user
from src.domain.usecases.chat.get import GetChatUsecase
from src.domain.usecases.common.user_existence import CheckUserExistenceUsecase
from src.domain.usecases.user.search import SearchUserUsecase

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@router.get("/search/{search_field}", status_code=status.HTTP_200_OK)
async def search_user(search_field: str, suu: Annotated[SearchUserUsecase, Depends(SearchUserUsecase)],
                      current_user=Depends(get_current_user)):
    try:
        found_users = await suu.search_user(search_field)
    except Exception as ex:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))
    return JSONResponse(status_code=HTTPStatus.CREATED, content={"users": str(found_users)})


@router.get("/{user_id}")
async def get_chat(user_id: int, cueu: Annotated[CheckUserExistenceUsecase, Depends(CheckUserExistenceUsecase)],
                   gcu: Annotated[GetChatUsecase, Depends(GetChatUsecase)],
                   current_user=Depends(get_current_user)):
    current_user_id = current_user.get("id")
    if not current_user_id:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    try:
        await cueu.check_user_existence_by_id(user_id)
    except Exception as ex:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))

    try:
        chat_content = await gcu.get_chat(current_user_id, user_id)
        return chat_content
    except Exception as ex:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(ex))


@router.websocket("/{user_id}/ws")
async def get_and_send_messages(websocket: WebSocket, current_user=Depends(get_current_user)):
    current_user_id = current_user.get("id")
    if not current_user_id:
        await websocket.close(code=1008)
        return

    await websocket.accept()
    while True:
        message_content = await websocket.receive_text()
        await websocket.send_text(message_content)
        try:
            pass
        except Exception:
            pass
