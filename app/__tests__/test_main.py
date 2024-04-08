"""tests for the main app"""

import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    """health check test"""
    response = await client.get("/")
    assert response.status_code == status.HTTP_200_OK
