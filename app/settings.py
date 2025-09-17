from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, env_prefix="APP_", extra="ignore")

    ENV: str = "development" #change to production in Cloud Run also .env
    SECRET_KEY: str = "change-me"
    DATABASE_URL: str = "sqlite:///.app.db"
    REDIS_URL: str = "redis://localhost:6379/0"

settings = Settings() #import anywhere to read config