from fastapi import Cookie, HTTPException
from src.security.jwt import verify_access_token


def set_auth_cookie(response, token: str):

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )


def delete_auth_cookie(response):

    response.delete_cookie(key="access_token")


def get_current_user_cookie(access_token: str = Cookie(None)):

    if access_token is None:
        raise HTTPException(
            status_code=401,
            detail="Login Required"
        )

    payload = verify_access_token(access_token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload
