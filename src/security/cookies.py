from fastapi import Cookie
from src.security.jwt import verify_access_token
from src.exceptions.handlers import LoginRequiredException, InvalidAccessTokenException


# ─── Access Token ────────────────────────────────────────────────────────────

def set_access_cookie(response, token: str):
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax"
    )


def delete_access_cookie(response):
    response.delete_cookie(key="access_token")


# ─── Refresh Token ────────────────────────────────────────────────────────────

def set_refresh_cookie(response, token: str, max_age_days: int = 7):
    response.set_cookie(
        key="refresh_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=max_age_days * 24 * 60 * 60   # convert days → seconds
    )


def delete_refresh_cookie(response):
    response.delete_cookie(key="refresh_token")


# ─── Convenience helpers (set / delete both at once) ─────────────────────────

def set_auth_cookies(response, access_token: str, refresh_token: str):
    set_access_cookie(response, access_token)
    set_refresh_cookie(response, refresh_token)


def delete_auth_cookies(response):
    delete_access_cookie(response)
    delete_refresh_cookie(response)


# ─── Legacy alias (keeps existing routes working) ────────────────────────────

def set_auth_cookie(response, token: str):
    set_access_cookie(response, token)


def delete_auth_cookie(response):
    delete_access_cookie(response)


# ─── Cookie-based user dependency (used by non-refresh-aware routes) ─────────

def get_current_user_cookie(access_token: str = Cookie(None)):

    if access_token is None:
        raise LoginRequiredException()

    payload = verify_access_token(access_token)

    if payload is None:
        raise InvalidAccessTokenException()

    return payload
