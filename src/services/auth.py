import bcrypt
import jwt
from jwt import PyJWTError

from src.settings.general import gc


class PasswordService:
    @staticmethod
    def generate_hashed_password(user_password: str) -> str:
        password_bytes = user_password.encode('utf-8')
        password_salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password_bytes, password_salt)

        password_string = password_hashed.decode('utf-8')
        return password_string

    @classmethod
    def create_password(cls, user_password) -> str:
        user_password = cls.generate_hashed_password(user_password)
        return user_password


class JWTService:
    @classmethod
    def sign_jwt(cls, user_id, username) -> dict:
        try:
            payload = {
                "id": user_id,
                "username": username,
                "expires": gc.JWT_TIME_EXPIRE
            }
            token = jwt.encode(payload, gc.JWT_SECRET_KEY, algorithm=gc.JWT_ALGORITHM)
        except PyJWTError as ex:
            raise ex
        return token

    @classmethod
    def decode_jwt(cls, token) -> dict:
        try:
            payload = jwt.decode(token, gc.JWT_SECRET_KEY, algorithms=[gc.JWT_ALGORITHM])
            return payload
        except PyJWTError as ex:
            raise ex
