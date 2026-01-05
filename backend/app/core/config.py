import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CLERK_SECRET_KEY : str = os.getenv("CLERK_SECRET_KEY", "")
    CLERK_PUBLISHABLE_KEY : str = os.getenv("CLERK_PUBLISHABLE_KEY", "")
    CLERK_JWKS_URL : str = os.getenv("CLERK_JWKS_URL", "")
    CLERK_WEBHOOK_SECRET : str = os.getenv("CLERK_WEBHOOK_SECRET", "")
    
    DATABASE_URL : str = os.getenv("DATABASE_URL", "sqlite:///./taskboard.db")
    FRONTEND_URL : str = os.getenv("FRONTEND_URL", "http://localhost:5173")
    
    FREE_TIER_MEMBERSHIP_LIMIT : int = 2
    PRO_TIER_MEMBERSHIP_LIMIT : int = 0 # 0 indicates no limit (unlimited)
    
settings = Config()