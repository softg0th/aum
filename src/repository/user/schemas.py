from pydantic import BaseModel, Field


class GenericUser(BaseModel):
    user_id: int = Field(...)
    username: str = Field(...)

