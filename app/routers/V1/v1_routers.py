"""
v1 routes file
all the v1 routes like auth
profile... will be included here
"""

from fastapi import APIRouter
from app.routers.V1.auth import auth_router

""" initialize the router """
router = APIRouter()

""" include auth routes """
router.include_router(auth_router.router)
