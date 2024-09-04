import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_NAME = os.environ.get("DB_NAME")
POSTGRES_USER = os.environ.get("DB_USER")
POSTGRES_PASSWORD = os.environ.get("DB_PASS")
