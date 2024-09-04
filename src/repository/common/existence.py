from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.infra.postgresql.models import User
from src.repository.common.schemas import IDUser
from src.repository.user.exceptions import UserNotFoundError


class ExistenceRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def check_user_existence_by_id(self, user_id: int):
        async with self._db as session:
            user_to_find = IDUser(id=user_id)
            stmt = select(User.username).where(User.id == user_to_find.id)
            result = await session.execute(stmt)
            found_user = result.fetchone()
            if not found_user:
                raise UserNotFoundError
