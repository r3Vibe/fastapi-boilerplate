"""
main routes file
all the v1 and v2... routes will go here
"""

from fastapi import APIRouter
from app.routers.V1 import v1_routers

""" initialize the router """
router = APIRouter()

""" include the v1 routes here """
router.include_router(v1_routers.router)
