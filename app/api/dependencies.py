import logging
import uuid
from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings  # Import settings for SECRET_KEY
from app.core.database import get_async_session
from app.models.user import User

# Set up logger for this module
logger = logging.getLogger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Manages user-related operations like password hashing, validation etc.
    """

    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request=None):
        logger.info(f"User {user.id} has registered.")
        # Add logic here if needed (e.g., send welcome email - requires email setup)

    async def on_after_forgot_password(self, user: User, token: str, request=None):
        logger.info(f"User {user.id} has forgot their password. Reset token: {token}")
        # Send password reset email here (requires email setup)

    async def on_after_request_verify(self, user: User, token: str, request=None):
        logger.info(f"Verification requested for user {user.id}. Verification token: {token}")
        # Send verification email here (requires email setup)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """Dependency to get the user database adapter."""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
) -> AsyncGenerator[UserManager]:
    """
    FastAPI Dependency to yield the UserManager instance.
    """
    yield UserManager(user_db)
