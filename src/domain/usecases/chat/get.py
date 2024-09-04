from src.infra.postgresql.db import get_session
from src.repository.chat.chat import ChatRepository


class GetChatUsecase:
    def __init__(self):
        self._session = get_session()

    async def get_chat(self, user_1_id: int, user_2_id: int):
        try:
            cr = ChatRepository(self._session)
            chat_content = await cr.get_chat_for_two_users(user_1_id, user_2_id)
        except Exception as ex:
            raise ex
        return chat_content
