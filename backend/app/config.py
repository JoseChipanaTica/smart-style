from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    API_V1_STR: str = "/smart-stlye/v1"

    OPENAI_API_KEY: str

    SUPABASE_URL: str
    SUPABASE_KEY: str

    STABILITY_API_KEY: str


settings = Settings()
