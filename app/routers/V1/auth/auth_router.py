"""
auth routes file
all the auth related routes will
be defined here
"""

from fastapi import APIRouter
from app.schemas.users import UserRegistration
from app.operations import users

""" initialize the router """
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
async def register_user(user: UserRegistration):
    """create user endpoint"""
    new_user = await users.create_user(user.model_dump())
    return new_user
