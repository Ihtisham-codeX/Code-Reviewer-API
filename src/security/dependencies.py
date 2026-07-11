from fastapi import Cookie
from src.security.jwt import verify_access_token
from src.exceptions.handlers import LoginRequiredException, InvalidAccessTokenException


# Called whenever a route uses Depends(get_current_user)
# Reads the JWT from the cookie, verifies it, and returns the user payload

def get_current_user(access_token: str = Cookie(None)):

    if access_token is None:
        raise LoginRequiredException()

    payload = verify_access_token(access_token)

    if payload is None:
        raise InvalidAccessTokenException()

    return payload
