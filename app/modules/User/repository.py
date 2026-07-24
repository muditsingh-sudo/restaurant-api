from app.modules.User.model import User
from app.modules.User.schema import UserCreate


class UserRepository:
    """Handles direct Tortoise ORM database operations for the User entity."""

    async def get_all(self) -> list[User]:
        return await User.all()

    async def get_by_id(self, user_id: int) -> User | None:
        return await User.get_or_none(id=user_id)

    async def get_by_email(self, email: str) -> User | None:
        return await User.get_or_none(email=email)

    async def create(self, user_data: UserCreate) -> User:
        return await User.create(**user_data.model_dump())

    async def save(self, user: User) -> User:
        await user.save()
        return user
