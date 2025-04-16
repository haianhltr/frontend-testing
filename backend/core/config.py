from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Auto-Remediation Platform"
    environment: str = "dev"

settings = Settings()
