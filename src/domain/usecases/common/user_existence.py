from src.infra.postgresql.db import get_session
from src.repository.common.existence import ExistenceRepository


class CheckUserExistenceUsecase:
    def __init__(self):
        self._session = get_session()

    async def check_user_existence_by_id(self, user_id: int):
        er = ExistenceRepository(self._session)
        try:
            await er.check_user_existence_by_id(user_id)
        except Exception as ex:
            raise ex
