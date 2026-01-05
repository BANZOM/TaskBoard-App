import httpx
from fastapi import Depends, HTTPException, status, Request
from clerk_backend_api.security import AuthenticateRequestOptions
from app.core.clerk import clerk
from app.core.config import settings

class AuthUser:
    def __init__(self, user_id: str, org_id: str, org_permissions: list[str]):
        self.user_id = user_id
        self.org_id = org_id
        self.org_permissions = org_permissions
        
    def has_permission(self, permission: str) -> bool:
        return permission in self.org_permissions
    
    @property
    def can_view(self) -> bool:
        return self.has_permission("org:tasks:view")
    
    @property
    def can_edit(self) -> bool:
        return self.has_permission("org:tasks:edit")
    
    @property
    def can_create(self) -> bool:
        return self.has_permission("org:tasks:create")
    
    @property
    def can_delete(self) -> bool:
        return self.has_permission("org:tasks:delete")
        