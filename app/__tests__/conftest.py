"""setup testing for the app"""

import pytest_asyncio
from httpx import AsyncClient
from app.main import app
from asgi_lifespan import LifespanManager
from app.database.db import get_db
from app.config.settings import settings
import os


@pytest_asyncio.fixture
async def get_app():
    """
    app fixture to get the app instacne
    and also generate a test database
    """
    os.environ["TEST_MODE"] = "True"  # set test mode to true for db creation
    async with LifespanManager(app) as manager:
        """
        lifespan method called and db created
        with that we will return the app instance
        """
        yield manager.app
    """after app is closed we will drop the databse"""
    try:
        client = await get_db()
        db_name = f"test_{settings.DB_NAME}"
        await client.drop_database(db_name)
    except Exception as e:
        print(e)
    finally:
        client.close()


@pytest_asyncio.fixture
async def client(get_app):
    """fixture to get the client instance of the app"""
    async with AsyncClient(
        app=get_app, base_url="http://127.0.0.1:8000/api/v1"
    ) as client:
        yield client
