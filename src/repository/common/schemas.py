from pydantic import BaseModel, Field


class IDUser(BaseModel):
    id: int = Field(...)
