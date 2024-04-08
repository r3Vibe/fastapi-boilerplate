""" all fastapi settings goes here that are coming from .env file """

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """get the data from the .env file"""

    DB_URL: str = Field(validation_alias="DB_URL")
    DB_NAME: str = Field(validation_alias="DB_NAME")
    TEST_MODE: bool = Field(validate_alias="TEST_MODE")

    class Config:
        env_file = ".env"


""" initialize the settings """
settings = Settings()
