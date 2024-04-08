""" mongodb database connection """

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings
from app.models.user_model import Users
import os


async def get_db():
    # Create Motor client
    client = AsyncIOMotorClient(settings.DB_URL)

    # get database name
    if os.environ["TEST_MODE"]:
        db_name = f"test_{settings.DB_NAME}"
    else:
        db_name = settings.DB_NAME

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client[db_name], document_models=[Users])

    return client
