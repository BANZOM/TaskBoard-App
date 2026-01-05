from clerk_backend_api import Clerk as ClerkBackendAPI
from app.core.config import settings

clerk = ClerkBackendAPI(
    bearer_auth=settings.CLERK_SECRET_KEY
)