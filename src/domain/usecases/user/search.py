from src.infra.postgresql.db import get_session
from src.infra.redis.cache import RedisClient
from src.repository.user.user import UserRepository


class SearchUserUsecase:
    def __init__(self):
        self._session = get_session()
        self._cache = RedisClient()

    async def search_user(self, pattern):
        try:
            ur = UserRepository(self._session, self._cache)
            found_users = await ur.find_user(pattern)
            return found_users
        except Exception as ex:
            raise ex
