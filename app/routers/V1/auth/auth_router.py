"""
auth routes file
all the auth related routes will
be defined here
"""

from fastapi import APIRouter

""" initialize the router """
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/test")
def test():
    """this is to test if the api is working"""
    return "ok"
