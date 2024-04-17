from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi import Depends
from typing import AsyncGenerator

from auth.models import User

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///database/db.sql'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

async def get_user_db(session: AsyncSession=Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
