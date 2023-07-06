from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn

load_dotenv()

class Settings(BaseSettings):
    database_url: str

settings = Settings()