import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .config import settings

logger = logging.getLogger(__name__)

# Create the async engine
# echo=True is useful for debugging SQL statements in development
async_engine = create_async_engine(
    str(settings.ASYNC_SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True, # Helps prevent errors from stale connections
    echo=settings.APP_ENV == "development", # Log SQL only in dev
    future=True, # Use SQLAlchemy 2.0 style
)

# Create the async session maker
AsyncSessionFactory = async_sessionmaker(
    bind=async_engine,
    autoflush=False,    # Recommended for async
    expire_on_commit=False, # Recommended for async / FastAPI background tasks
    class_=AsyncSession # Specify AsyncSession class
)

# --- Dependency for FastAPI Routes ---
async def get_async_session() -> AsyncGenerator[AsyncSession]:
    """
    FastAPI dependency that provides an AsyncSession for a request.
    Ensures the session is closed afterwards.
    """
    logger.debug("Creating async session")
    async with AsyncSessionFactory() as session:
        try:
            yield session
            # Optionally commit here if you want automatic commit per request
            # await session.commit() # Be careful with this pattern
            logger.debug("Session yielded")
        except Exception:
            logger.exception("Session rollback because of exception")
            await session.rollback()
            raise
        finally:
            # The 'async with' context manager handles closing automatically
            logger.debug("Session closed")
