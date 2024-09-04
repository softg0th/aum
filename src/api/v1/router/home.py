from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/home",
    tags=["home"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def homepage():
    pass
