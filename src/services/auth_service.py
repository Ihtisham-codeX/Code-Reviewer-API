from datetime import datetime, timedelta
from src.security.hashing import hash_password, verify_password
from src.security.jwt import create_access_token, create_refresh_token, verify_refresh_token
from src.respositories import user_repo
from src.respositories import token_repo
from src.config import settings
from src.exceptions.handlers import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    InvalidRefreshTokenException,
    RefreshTokenRevokedException
)


########################### SIGNUP ###########################
def signup(email: str, password: str):

    # Check if user already exists
    existing = user_repo.find_user_by_email(email)
    if existing:
        raise UserAlreadyExistsException()

    # Hash the password
    hashed = hash_password(password)

    # Save the new user
    row = user_repo.create_user(email, hashed)

    return {
        "message": "Signup Successful",
        "user_id": row[0],
        "email": row[1]
    }


########################### LOGIN ###########################
def login(email: str, password: str):

    # Find user by email
    row = user_repo.find_user_by_email(email)

    # User not found
    if row is None:
        raise InvalidCredentialsException()

    # Verify password
    if not verify_password(password, row[2]):
        raise InvalidCredentialsException()

    token_data = {
        "user_id": row[0],
        "email": row[1]
    }

    # Create access token (short-lived)
    access_token = create_access_token(token_data)

    # Create refresh token (long-lived)
    refresh_token = create_refresh_token(token_data)

    # Persist refresh token in DB
    expires_at = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS)
    token_repo.save_refresh_token(row[0], refresh_token, expires_at)

    return access_token, refresh_token


########################### REFRESH ###########################
def refresh(refresh_token: str):

    # 1. Verify the JWT signature and type claim
    payload = verify_refresh_token(refresh_token)
    if payload is None:
        raise InvalidRefreshTokenException()

    # 2. Check the token actually exists in DB (not revoked / rotated away)
    db_token = token_repo.find_refresh_token(refresh_token)
    if db_token is None:
        raise RefreshTokenRevokedException()

    # 3. Delete the OLD refresh token (token rotation — one-time use)
    token_repo.revoke_refresh_token(refresh_token)

    user_id = payload.get("user_id")
    email   = payload.get("email")

    token_data = {
        "user_id": user_id,
        "email": email
    }

    # 4. Issue a brand-new access + refresh token pair
    new_access_token  = create_access_token(token_data)
    new_refresh_token = create_refresh_token(token_data)

    # 5. Persist the new refresh token
    expires_at = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS)
    token_repo.save_refresh_token(user_id, new_refresh_token, expires_at)

    return new_access_token, new_refresh_token


########################### LOGOUT ###########################
def logout(refresh_token: str | None):

    # Revoke the refresh token from DB so it can never be reused
    if refresh_token:
        token_repo.revoke_refresh_token(refresh_token)
