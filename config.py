from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST : str
    DATABASE_PORT : int
    class Config:
        env_file = ".env"