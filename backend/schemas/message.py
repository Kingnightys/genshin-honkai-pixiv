# d:\AiCodeProject\genshin-honkai-pixiv\backend\schemas\message.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MessageCreate(BaseModel):
    user_id: Optional[int] = Field(1, description="用户ID")
    nickname: str = Field(..., description="昵称")
    email: Optional[str] = Field(None, description="邮箱")
    content: str = Field(..., description="留言内容")

class MessageResponse(BaseModel):
    id: int = Field(..., description="留言ID")
    user_id: int = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    email: Optional[str] = Field(None, description="邮箱")
    content: str = Field(..., description="留言内容")
    created_at: datetime = Field(..., description="创建时间")
    
    model_config = {
        "from_attributes": True
    }