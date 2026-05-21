from fastapi import APIRouter, HTTPException
from datetime import datetime

router = APIRouter(prefix="/messages", tags=["messages"])

messages_db = []
message_id_counter = 1

@router.get("/")
async def get_messages():
    return {"data": messages_db}

@router.post("/")
async def create_message(content: dict):
    global message_id_counter
    try:
        message = {
            "id": message_id_counter,
            "user_id": 1,
            "nickname": content.get("nickname", "匿名用户"),
            "email": content.get("email", ""),
            "content": content.get("content", ""),
            "created_at": int(datetime.now().timestamp())
        }
        message_id_counter += 1
        messages_db.append(message)
        return {"data": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail="创建留言失败")
