from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Chat(Base):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_1_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user_2_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self):
        return f"Chat({self.id}, {self.user_1_id}, {self.user_2_id})"
