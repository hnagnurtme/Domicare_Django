from typing import Optional

from pydantic import BaseModel


class RoleDTO(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True  # For ORM compatibility