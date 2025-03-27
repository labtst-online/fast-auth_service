from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from app.core.config import settings  # Import settings for secret and lifetime

# --- Bearer Token Transport ---
# Defines how the token is transmitted (e.g., Authorization: Bearer <token>)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login") # Point to the login endpoint

# --- JWT Strategy ---
# Defines how tokens are generated and validated
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=settings.JWT_LIFETIME_SECONDS
    )

# --- Authentication Backend ---
# Combines transport and strategy
# name="jwt" is important, used in router prefixes
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
