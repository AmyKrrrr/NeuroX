from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Agentic Research Backend"
    ENV: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()

