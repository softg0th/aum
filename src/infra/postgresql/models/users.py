from datetime import date

from sqlalchemy import String, DateTime, func, ARRAY, INT
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(250))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    contacts: Mapped[ARRAY] = mapped_column(ARRAY(INT), nullable=True)

    def __repr__(self):
        return f"User({self.id}, {self.username})"
