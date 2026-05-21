# d:\AiCodeProject\genshin-honkai-pixiv\backend\routes\auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import hashlib
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse, TokenResponse

router = APIRouter(tags=["auth"])

@router.post("/token", response_model=TokenResponse)
async def login(username: str, password: str, db: Session = Depends(get_db)):
    """用户登录"""
    if not username or not password:
        raise HTTPException(status_code=400, detail="缺少用户名或密码")
    
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="用户不存在")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user.hashed_password != hashed_password:
        raise HTTPException(status_code=401, detail="密码错误")
    
    return {"access_token": f"token_{user.id}_{username}", "token_type": "bearer"}

@router.post("/register", response_model=TokenResponse)
async def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    """用户注册"""
    if not username or not email or not password:
        raise HTTPException(status_code=400, detail="缺少必要信息")
    
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="用户名已存在")
    
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="邮箱已被注册")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"access_token": f"token_{user.id}_{username}", "token_type": "bearer"}

@router.get("/users/me", response_model=UserResponse)
async def get_current_user(db: Session = Depends(get_db)):
    """获取当前用户信息"""
    # 简化实现，返回第一个用户作为演示
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户未找到")
    return user