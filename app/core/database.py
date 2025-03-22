from typing import AsyncGenerator

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import get_settings

settings = get_settings()

engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))


Async_Session = async_sessionmaker(engine, expire_on_commit=False)

async def get_db(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with Async_Session() as session:
        yield session
