from pydantic import BaseModel, Field


class GenericChat(BaseModel):
    user_1_id: int = Field(...)
    user_2_id: int = Field(...)
