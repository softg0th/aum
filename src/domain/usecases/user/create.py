from src.infra.postgresql.db import get_session
from src.repository.user.user import UserRepository


class CreateUserUsecase:
    def __init__(self):
        self._session = get_session()
        
    async def create_user(self, user):
        try:
            ur = UserRepository(self._session)
            await ur.insert_user(user)
        except Exception as ex:
            raise ex
