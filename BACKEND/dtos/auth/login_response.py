from pydantic import BaseModel, Field
from dtos.user_dto import UserDTO


class LoginResponse(BaseModel):
    access_token: str = Field(..., alias="accessToken")
    refresh_token: str = Field(..., alias="refreshToken")
    user: UserDTO

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "refreshToken": "550e8400-e29b-41d4-a716-446655440000",
                "user": {
                    "id": 1,
                    "email": "user@example.com",
                    "name": "John Doe"
                }
            }
        }