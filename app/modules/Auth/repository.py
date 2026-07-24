from app.modules.User.model import User


class AuthRepository:
    """Handles direct Tortoise ORM database operations for authentication verification."""

    async def get_user_by_email(self, email: str) -> User | None:
        """Fetches a user profile from the database matching the provided email."""
        return await User.get_or_none(email=email)
