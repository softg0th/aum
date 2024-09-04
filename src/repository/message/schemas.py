import datetime

from pydantic import BaseModel, Field


class GenericMessageChatRelation(BaseModel):
    chat_id: int = Field(...)


class GenericMessage(BaseModel):
    sender_username: str = Field(...)
    sent_at: datetime.date = Field(...)
    text: str = Field(...)
