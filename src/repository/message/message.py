from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.infra.postgresql.models import Message
from src.repository.message.schemas import GenericMessageChatRelation, GenericMessage


class MessageRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def grep_all_messages_in_chat(self, chat_id: int) -> List[GenericMessage]:
        async with self._db as session:
            chat_message_structure = GenericMessageChatRelation(chat_id=chat_id)
            stmt = select(Message.sender_username, Message.sent_at,
                          Message.text).where(Message.chat_id ==
                                              chat_message_structure.chat_id).order_by(Message.sent_at)
            result = await session.execute(stmt)
            found_messages = result.fetchall()
            if found_messages:
                found_output = [GenericMessage(sender_username=message.sender_usernam[0],
                                               sent_at=message.sent_at[0], text=message.text[0])
                                for message in found_messages]
                return found_output
            return [GenericMessage()]

    async def add_new_message(self, chat_id, user):