from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers

from database.database import SessionLocal, engine, Base
from auth.router import router as router_auth
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.models import User

app = FastAPI(title='Chat App')

async def get_db():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

app.include_router(router_auth)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/user/login",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/user/registration",
    tags=["auth"],
)
