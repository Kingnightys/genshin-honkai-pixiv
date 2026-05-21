# d:\AiCodeProject\genshin-honkai-pixiv\backend\schemas\user.py
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    
    model_config = {
        "from_attributes": True
    }

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str