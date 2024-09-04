from sqlalchemy import select, or_, and_
from sqlalchemy.orm import selectinload
from sqlmodel.ext.asyncio.session import AsyncSession

from src.infra.postgresql.models import Chat
from src.repository.chat.schemas import GenericChat
from src.repository.message.message import MessageRepository


class ChatRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def _create_chat_for_two_users(self, chat: GenericChat):
        async with self._db as session:
            session.add(chat)
        try:
            await session.commit()
        except Exception as ex:
            raise ex

    async def get_chat_for_two_users(self, user_id1: int, user_id2: int):
        async with self._db as session:
            user_chat_structure = GenericChat(user_1_id=user_id1, user_2_id=user_id2)
            stmt = select(Chat).filter(
                or_(
                    and_(Chat.user_1_id == user_chat_structure.user_1_id, Chat.user_2_id ==
                         user_chat_structure.user_2_id),
                    and_(Chat.user_1_id == user_chat_structure.user_2_id,
                         Chat.user_2_id == user_chat_structure.user_1_id)
                )
            )
            result = await session.execute(stmt)
            found_chat = result.fetchone()
            chat_id = found_chat.id[0]
            if found_chat:
                mr = MessageRepository(self._db)
                messages = await mr.grep_all_messages_in_chat(int(chat_id))
                return messages
            else:
                await self._create_chat_for_two_users(user_chat_structure)
