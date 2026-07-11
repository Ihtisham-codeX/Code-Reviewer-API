from fastapi import APIRouter, Response
from src.models.auth import UserSignup, UserLogin
from src.services import auth_service
from src.security.cookies import set_auth_cookie, delete_auth_cookie

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Signup
@router.post("/signup")
def signup(user: UserSignup):
    return auth_service.signup(user.email, user.password)


# Login
@router.post("/login")
def login(user: UserLogin, response: Response):
    token = auth_service.login(user.email, user.password)
    set_auth_cookie(response, token)
    return {"message": "Login Successful"}


# Logout
@router.post("/logout")
def logout(response: Response):
    delete_auth_cookie(response)
    return {"message": "Logged Out Successfully"}
