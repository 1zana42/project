import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME: str
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )
    
    @property
    def get_db_url(self):
        return f"sqlite+aiosqlite:///{self.DB_NAME}"

    @property
    def auth_data(self):
        return {"algorithm": {self.JWT_ALGORITHM}, "secret_key": {self.JWT_SECRET_KEY}}


settings = Settings()
