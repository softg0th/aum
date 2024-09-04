from datetime import date
from typing import List

import bcrypt
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.repository.common.errors import CacheNotInitializedException
from src.infra.redis.cache import RedisClient
from src.repository.user.exceptions import UserAlreadyExistsError, UserNotFoundError, UserPasswordIncorrectError
from src.infra.postgresql.models import User
from src.repository.user.schemas import GenericUser


class UserRepository:
    def __init__(self, session: AsyncSession, cache=None):
        self._db = session
        self._cache = cache

    async def _check_cache(self):
        if not isinstance(self._cache, RedisClient):
            raise CacheNotInitializedException

    async def insert_user(self, external_user):
        async with self._db as session:
            pretty_user = User(username=external_user.username, password=external_user.password,
                               created_at=date.today(), contacts=[])
            session.add(pretty_user)
            try:
                await session.commit()
            except IntegrityError:
                raise UserAlreadyExistsError

    async def check_user(self, external_user) -> GenericUser:
        async with self._db as session:
            pretty_user = User(username=external_user.username, password=external_user.password)
            stmt = select(User.username, User.password).where(User.username == pretty_user.username)
            result = await session.execute(stmt)
            found_user = result.fetchone()
            if not found_user:
                raise UserNotFoundError
            if not bcrypt.checkpw(external_user.password.encode('utf-8'), found_user.password.encode('utf-8')):
                raise UserPasswordIncorrectError
            logged_user = GenericUser(user_id=found_user.id[0], username=external_user.username)
            return logged_user

    async def find_user(self, pattern) -> List[str]:
        try:
            await self._check_cache()
        except Exception as ex:
            raise ex

        self._cache.db = 0
        stored_users = await self._cache.get(pattern)
        if stored_users:
            return stored_users.split()
        async with self._db as session:
            stmt = select(User.username).where(User.username.like(pattern)).limit(10)
            result = await session.execute(stmt)
            found_users = result.fetchall()
            found_output = [user.username[0] for user in found_users]

            if len(found_output) > 0:
                await self._cache.set(pattern, str(found_output))
            return found_output
