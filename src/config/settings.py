import os


# JWT Settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
# access token used my all middlewares
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 30))
# refersh token is different , it is used to generate new access token within its time limit
JWT_REFRESH_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_EXPIRE_DAYS", 7))

# Gemini AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App
COOKIE_DOMAIN = os.getenv("COOKIE_DOMAIN", "localhost")
MAX_REVIEWS_PER_HOUR = int(os.getenv("MAX_REVIEWS_PER_HOUR", 5))
