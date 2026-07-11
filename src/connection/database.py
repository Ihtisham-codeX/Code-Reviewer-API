import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = None

try:
    conn = psycopg2.connect(
        database=os.getenv("PG_DATABASE"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        sslmode=os.getenv("PG_SSLMODE")
    )
    print("Database Connected")

except Exception as e:
    print(f"Database Connection Failed: {e}")
    raise RuntimeError(f"Could not connect to the database: {e}")
