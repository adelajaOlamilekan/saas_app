from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
  SECRET_KEY: str
  ALGORITHM: str
  ACCESS_TOKEN_MINUTES: float

settings = AppSettings()