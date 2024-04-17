from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr

class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    
    class Config:
        orm_code = True

class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

# then
class UserUpdate(schemas.BaseUserUpdate):
    pass
