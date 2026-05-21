from fastapi import APIRouter, HTTPException
import hashlib

router = APIRouter(tags=["auth"])

users_db = {
    "admin": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "password": hashlib.sha256("123456".encode()).hexdigest(),
        "is_active": True
    }
}

@router.post("/token")
async def login(username: str = None, password: str = None):
    if not username or not password:
        raise HTTPException(status_code=400, detail="缺少用户名或密码")
    
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=401, detail="用户不存在")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user["password"] != hashed_password:
        raise HTTPException(status_code=401, detail="密码错误")
    
    return {"access_token": f"mock_token_{username}", "token_type": "bearer"}

@router.post("/register")
async def register(username: str = None, email: str = None, password: str = None):
    if not username or not email or not password:
        raise HTTPException(status_code=400, detail="缺少必要信息")
    
    if username in users_db:
        raise HTTPException(status_code=400, detail="用户名已存在")
    
    users_db[username] = {
        "id": len(users_db) + 1,
        "username": username,
        "email": email,
        "password": hashlib.sha256(password.encode()).hexdigest(),
        "is_active": True
    }
    
    return {"access_token": f"mock_token_{username}", "token_type": "bearer"}

@router.get("/users/me")
async def get_current_user():
    return users_db.get("admin", {})
