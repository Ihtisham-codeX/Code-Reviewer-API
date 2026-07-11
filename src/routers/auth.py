from fastapi import APIRouter, Response, Cookie
from src.models.auth import UserSignup, UserLogin
from src.services import auth_service
from src.security.cookies import set_auth_cookies, delete_auth_cookies
from src.exceptions.handlers import MissingRefreshTokenException

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ─── Signup ───────────────────────────────────────────────────────────────────
@router.post("/signup")
def signup(user: UserSignup):
    return auth_service.signup(user.email, user.password)


# ─── Login ────────────────────────────────────────────────────────────────────
@router.post("/login")
def login(user: UserLogin, response: Response):
    access_token, refresh_token = auth_service.login(user.email, user.password)
    set_auth_cookies(response, access_token, refresh_token)
    return {"message": "Login Successful"}


# ─── Refresh ──────────────────────────────────────────────────────────────────
@router.post("/refresh")
def refresh(response: Response, refresh_token: str = Cookie(None)):

    if refresh_token is None:
        raise MissingRefreshTokenException()

    new_access_token, new_refresh_token = auth_service.refresh(refresh_token)
    set_auth_cookies(response, new_access_token, new_refresh_token)
    return {"message": "Tokens Refreshed Successfully"}


# ─── Logout ───────────────────────────────────────────────────────────────────
@router.post("/logout")
def logout(response: Response, refresh_token: str = Cookie(None)):
    auth_service.logout(refresh_token)      # revoke in DB
    delete_auth_cookies(response)           # clear both cookies
    return {"message": "Logged Out Successfully"}
