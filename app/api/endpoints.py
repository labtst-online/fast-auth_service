from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.api.dependencies import get_user_manager
from app.api.security import auth_backend
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

# Initialize FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# Auth routes (/login, /logout)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),  # Pass the specific backend
    prefix="/auth/jwt",  # Standard prefix
    tags=["Auth"],
)

# Register routes (/register)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# Reset password routes (/forgot-password, /reset-password)
# Note: Requires email sending capabilities to be fully functional
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)

# Verify routes (/request-verify-token, /verify)
# Note: Requires email sending capabilities and user model flag (is_verified)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth"],
)

# User management routes (/users/me, /users/{id})
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)
