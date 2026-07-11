from fastapi import Cookie, HTTPException
from src.security.jwt import verify_access_token


# Called whenever a route uses Depends(get_current_user)
# Reads the JWT from the cookie, verifies it, and returns the user payload

def get_current_user(access_token: str = Cookie(None)):

    if access_token is None:
        raise HTTPException(
            status_code=401,
            detail="Login Required"
        )

    payload = verify_access_token(access_token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    return payload
