from pydantic import BaseModel, Field, constr, model_validator
from typing_extensions import Self


class UserCreate(BaseModel):
    username: constr(max_length=50) = Field(..., description='User name')
    password: constr(min_length=8, max_length=250) = Field(..., description='Password')
    password_confirm: constr(min_length=8, max_length=250) = Field(..., description='Password confirm')

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        password_input = self.password
        password_confirmation = self.password_confirm

        if password_input != password_confirmation:
            raise ValueError('passwords do not match')
        return self


class UserLogin(BaseModel):     # i hate this combination so much...
    username: str = Field(..., description='User name')
    password: str = Field(..., description='Password')
