import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    # Add any extra fields from your User model you want to expose
    # Example: full_name: Optional[str] = None
    pass


class UserCreate(schemas.BaseUserCreate):
    # Add any extra fields required during registration
    # Example: full_name: str
    pass


class UserUpdate(schemas.BaseUserUpdate):
    # Add any extra fields allowed during user update
    # Example: full_name: Optional[str] = None
    pass
