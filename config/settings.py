from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
  SECRET_KEY: str
  ALGORITHM: str
  ACCESS_TOKEN_MINUTES: float
  GITHUB_CLIENT_ID: str
  GITHUB_CLIENT_SECRET: str
  GITHUB_AUTHORIZATION_URL: str
  GITHUB_REDIRECT_URL: str
  GITHUB_ACCESS_TOKEN_URL: str
  GITHUB_USER_API: str


settings = AppSettings()