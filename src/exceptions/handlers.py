from fastapi import HTTPException

# __init__ is a constructor that automatically runs when the object is calles
# super() used to first run the parent constructor
# self is an empty object created

class ProjectNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Project not found"
        )


class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Email already registered"
        )


class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid email or password"
        )


class RateLimitExceededException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=429,
            detail="Rate limit exceeded. Max 5 reviews per hour."
        )


class UnsupportedFileTypeException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Unsupported file type"
        )
