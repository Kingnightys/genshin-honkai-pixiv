# d:\AiCodeProject\genshin-honkai-pixiv\backend\init_db.py
from database import engine, Base
from models.user import User
from models.message import Message

# 创建所有表
def init_database():
    Base.metadata.create_all(bind=engine)
    print("数据库表创建成功")

if __name__ == "__main__":
    init_database()