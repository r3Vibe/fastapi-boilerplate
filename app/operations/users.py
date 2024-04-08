from app.models.user_model import Users
from app.schemas.users import UserRegistration


async def create_user(user: UserRegistration) -> Users:
    new_user = Users(**user)
    await new_user.insert()
    return new_user
