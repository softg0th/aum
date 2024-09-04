from contextlib import asynccontextmanager

from pydantic.networks import PostgresDsn
from pydantic_core import MultiHostUrl
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_NAME, POSTGRES_USER, POSTGRES_PASSWORD
from .models import Base


def get_postgres_dsn() -> PostgresDsn:
    return MultiHostUrl.build(
        scheme="postgresql+asyncpg",
        host=POSTGRES_HOST,
        port=int(POSTGRES_PORT),
        username=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        path=POSTGRES_NAME
    )


#   DATABASE_URL = (f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
#                f"{POSTGRES_PORT}/{POSTGRES_NAME}")
DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost/aum-db"
async_engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
