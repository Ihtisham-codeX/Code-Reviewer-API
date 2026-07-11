from fastapi import HTTPException
from src.security.hashing import hash_password, verify_password
from src.security.jwt import create_access_token
from src.respositories import user_repo


########################### SIGNUP ###########################
def signup(email: str, password: str):

    # Check if user already exists
    existing = user_repo.find_user_by_email(email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

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
        raise HTTPException(
            status_code=401,
            detail="User does not exist"
        )

    # Verify password
    if not verify_password(password, row[2]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    # Create JWT token
    token = create_access_token({
        "user_id": row[0],
        "email": row[1]
    })

    return token
