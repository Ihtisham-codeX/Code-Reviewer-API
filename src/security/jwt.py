from jose import jwt, JWTError
from datetime import datetime, timedelta
from src.config import settings


def create_access_token(data: dict):

    # Make a copy of the data
    payload = data.copy()

    # Calculate expiration time
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)

    # Add exp to payload
    payload.update({
        "exp": expire
    })

    # Encode and return JWT
    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return token


def create_refresh_token(data: dict):

    # Make a copy of the data
    payload = data.copy()

    # Calculate expiration time (longer-lived)
    expire = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS)

    # Mark token type so it cannot be used as an access token
    payload.update({
        "exp": expire,
        "type": "refresh"
    })

    # Encode with separate refresh secret
    token = jwt.encode(
        payload,
        settings.JWT_REFRESH_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return token


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return payload

    except JWTError:
        return None


def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        # Ensure it is actually a refresh token
        if payload.get("type") != "refresh":
            return None

        return payload

    except JWTError:
        return None
