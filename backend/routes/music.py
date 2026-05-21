from fastapi import APIRouter

router = APIRouter(prefix="/music", tags=["music"])

default_music = [
    {"id": 1, "title": "璃月", "artist": "HOYO-MiX", "album": "原神OST", "game": "genshin", "duration": "4:32", "cover_url": "https://neeko-copilot.bytedance.net/api/text2image?prompt=liyue%20landscape%20album%20cover&width=256&height=256"},
    {"id": 2, "title": "稻妻", "artist": "HOYO-MiX", "album": "原神OST", "game": "genshin", "duration": "5:18", "cover_url": "https://neeko-copilot.bytedance.net/api/text2image?prompt=inazuma%20landscape%20album%20cover&width=256&height=256"},
    {"id": 3, "title": "星穹铁道", "artist": "HOYO-MiX", "album": "星穹铁道OST", "game": "starrail", "duration": "3:45", "cover_url": "https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20space%20album%20cover&width=256&height=256"},
]

@router.get("/")
async def get_music():
    return {"data": default_music}
