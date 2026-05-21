# d:\AiCodeProject\genshin-honkai-pixiv\backend\models\message.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)