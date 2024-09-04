from sqlalchemy import ForeignKey, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    sender_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    receiver_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str] = mapped_column()
    sent_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'Message({self.id}, {self.chat_id}, {self.sender_id})'
