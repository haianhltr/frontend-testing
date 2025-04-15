from pydantic_settings import BaseSettings  # ✅ new location in v2

class Settings(BaseSettings):
    app_name: str = "Auto-Remediation Platform"
    environment: str = "dev"

settings = Settings()
