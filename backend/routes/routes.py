# - API路由
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Character, Music, Video, FanArt, FanNovel, FanVideo, MapSpot, Anime, Message, User
from auth import get_current_active_user
from schemas import MessageCreate
import time

router = APIRouter()

# 角色路由
@router.get("/characters")
def get_characters(game: str = None, version: str = None, element: str = None, rarity: int = None, db: Session = Depends(get_db)):
    query = db.query(Character)
    if game:
        query = query.filter(Character.game == game)
    if version:
        query = query.filter(Character.version == version)
    if element:
        query = query.filter(Character.element == element)
    if rarity:
        query = query.filter(Character.rarity == rarity)
    return {"data": query.all()}

@router.get("/characters/{id}")
def get_character(id: int, db: Session = Depends(get_db)):
    char = db.query(Character).filter(Character.id == id).first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"data": char}

# 音乐路由
@router.get("/music")
def get_music(game: str = None, version: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(Music)
    if game:
        query = query.filter(Music.game == game)
    if version:
        query = query.filter(Music.version == version)
    if category:
        query = query.filter(Music.category == category)
    return {"data": query.all()}

@router.get("/music/{id}")
def get_music_by_id(id: int, db: Session = Depends(get_db)):
    music = db.query(Music).filter(Music.id == id).first()
    if not music:
        raise HTTPException(status_code=404, detail="Music not found")
    return {"data": music}

# 视频路由
@router.get("/videos")
def get_videos(game: str = None, version: str = None, db: Session = Depends(get_db)):
    query = db.query(Video)
    if game:
        query = query.filter(Video.game == game)
    if version:
        query = query.filter(Video.version == version)
    return {"data": query.all()}

@router.get("/videos/{id}")
def get_video(id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"data": video}

# Fan Arts
@router.get("/fanarts")
def get_fanarts(db: Session = Depends(get_db)):
    return {"data": db.query(FanArt).all()}

@router.get("/fanarts/{id}")
def get_fanart(id: int, db: Session = Depends(get_db)):
    art = db.query(FanArt).filter(FanArt.id == id).first()
    if not art:
        raise HTTPException(status_code=404, detail="Fan art not found")
    return {"data": art}

# Fan Novels
@router.get("/fannovels")
def get_fannovels(db: Session = Depends(get_db)):
    return {"data": db.query(FanNovel).all()}

@router.get("/fannovels/{id}")
def get_fannovel(id: int, db: Session = Depends(get_db)):
    novel = db.query(FanNovel).filter(FanNovel.id == id).first()
    if not novel:
        raise HTTPException(status_code=404, detail="Fan novel not found")
    return {"data": novel}

# Fan Videos
@router.get("/fanvideos")
def get_fanvideos(db: Session = Depends(get_db)):
    return {"data": db.query(FanVideo).all()}

@router.get("/fanvideos/{id}")
def get_fanvideo(id: int, db: Session = Depends(get_db)):
    video = db.query(FanVideo).filter(FanVideo.id == id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Fan video not found")
    return {"data": video}

# Map Spots
@router.get("/mapspots")
def get_mapspots(game: str = None, db: Session = Depends(get_db)):
    query = db.query(MapSpot)
    if game:
        query = query.filter(MapSpot.game == game)
    return {"data": query.all()}

@router.get("/mapspots/{id}")
def get_mapspot(id: int, db: Session = Depends(get_db)):
    spot = db.query(MapSpot).filter(MapSpot.id == id).first()
    if not spot:
        raise HTTPException(status_code=404, detail="Map spot not found")
    return {"data": spot}

# Animes
@router.get("/animes")
def get_animes(db: Session = Depends(get_db)):
    return {"data": db.query(Anime).all()}

@router.get("/animes/{id}")
def get_anime(id: int, db: Session = Depends(get_db)):
    anime = db.query(Anime).filter(Anime.id == id).first()
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return {"data": anime}

# Messages
@router.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    return {"data": db.query(Message).order_by(Message.created_at.desc()).all()}

@router.post("/messages")
def create_message(msg: MessageCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    new_msg = Message(
        user_id=current_user.id,
        nickname=current_user.username,
        email=current_user.email,
        content=msg.content,
        created_at=int(time.time())
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return {"data": new_msg}

# 统计信息
@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    return {
        "characters": db.query(Character).count(),
        "music": db.query(Music).count(),
        "videos": db.query(Video).count(),
        "users": db.query(User).count(),
        "messages": db.query(Message).count(),
    }

# 版本列表
@router.get("/versions")
def get_versions(game: str = None, db: Session = Depends(get_db)):
    result = {
        "genshin": [],
        "starrail": []
    }
    
    if game == "genshin" or game is None:
        genshin_versions = db.query(Character.version).filter(Character.game == "genshin").distinct().all()
        result["genshin"] = sorted([v[0] for v in genshin_versions if v[0]], key=lambda x: float(x.replace("版本", "")))
    
    if game == "starrail" or game is None:
        starrail_versions = db.query(Character.version).filter(Character.game == "starrail").distinct().all()
        result["starrail"] = sorted([v[0] for v in starrail_versions if v[0]], key=lambda x: float(x.replace("版本", "")))
    
    return result

@router.get("/version_info")
def get_version_info(db: Session = Depends(get_db)):
    genshin_versions = db.query(Character.version).filter(Character.game == "genshin").distinct().count()
    starrail_versions = db.query(Character.version).filter(Character.game == "starrail").distinct().count()
    
    genshin_chars = db.query(Character).filter(Character.game == "genshin").count()
    starrail_chars = db.query(Character).filter(Character.game == "starrail").count()
    
    return {
        "genshin": {
            "versions": genshin_versions,
            "characters": genshin_chars
        },
        "starrail": {
            "versions": starrail_versions,
            "characters": starrail_chars
        }
    }