from src.infra.postgresql.db import get_session
from src.repository.user.user import UserRepository


class CheckUserUsecase:
    def __init__(self):
        self._session = get_session()

    async def check_user(self, user):
        try:
            ur = UserRepository(self._session)
            logged_user = await ur.check_user(user)
        except Exception as ex:
            raise ex
        return logged_user
