from pathlib import Path
from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / '.env')


DATABASE_URL = (
    f"postgresql://"
    f"{getenv('DB_USER')}:"
    f"{getenv('DB_PASSWORD')}@"
    f"{getenv('DB_HOST')}:"
    f"{getenv('DB_PORT')}/"
    f"{getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)