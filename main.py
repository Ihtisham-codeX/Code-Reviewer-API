# Load environment variables first
from dotenv import load_dotenv

load_dotenv()

# FastAPI
from fastapi import FastAPI

# Routers
from src.routers.auth import router as auth_router
from src.routers.projects import router as projects_router
from src.routers.review import router as review_router
from src.routers.history import router as history_router
from src.routers.user import router as user_router

# Middleware
from src.middleware.logging import LoggingMiddleware

# Create FastAPI app
app = FastAPI(
    title="Code Reviewer API"
)

# Register middleware
app.add_middleware(LoggingMiddleware)

# Register routers
app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(review_router)
app.include_router(history_router)
app.include_router(user_router)
