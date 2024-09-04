from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.services.auth import JWTService

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials
    payload = JWTService.decode_jwt(token)
    return {'user_id': payload.get('user_id'), 'username': payload.get('username')}
