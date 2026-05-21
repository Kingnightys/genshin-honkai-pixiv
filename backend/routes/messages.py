# d:\AiCodeProject\genshin-honkai-pixiv\backend\routes\messages.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import get_db
from models.message import Message
from schemas.message import MessageCreate, MessageResponse

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/", response_model=list[MessageResponse])
async def get_messages(db: Session = Depends(get_db)):
    """获取所有留言"""
    messages = db.query(Message).order_by(Message.created_at.desc()).all()
    return messages

@router.post("/", response_model=MessageResponse)
async def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    """创建新留言"""
    try:
        db_message = Message(
            user_id=message.user_id,
            nickname=message.nickname,
            email=message.email,
            content=message.content
        )
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="创建留言失败")

@router.delete("/{message_id}")
async def delete_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="留言不存在")
    
    db.delete(message)
    db.commit()
    return {"message": "删除成功"}