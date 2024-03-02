""" mongodb database connection """

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings


async def get_db():
    # Create Motor client
    client = AsyncIOMotorClient(settings.DB_URL)

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client[settings.DB_NAME], document_models=[])
