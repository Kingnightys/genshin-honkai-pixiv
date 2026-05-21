# d:\AiCodeProject\genshin-honkai-pixiv\backend\schemas\message.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    nickname: str = Field(..., description="昵称")
    email: Optional[str] = Field(None, description="邮箱")
    content: str = Field(..., description="留言内容")

class MessageResponse(BaseModel):
    id: int
    user_id: int
    nickname: str
    email: Optional[str]
    content: str
    created_at: datetime