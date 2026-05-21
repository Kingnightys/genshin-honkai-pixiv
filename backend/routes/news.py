from fastapi import APIRouter, HTTPException
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.hoyoverse_service import HoyoverseService
from utils.logger import logger

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/", response_model=List[Dict])
async def get_news(game: str = "genshin"):
    """获取最新资讯"""
    if game not in ["genshin", "starrail"]:
        raise HTTPException(status_code=400, detail="Invalid game. Use 'genshin' or 'starrail'.")
    
    logger.info(f"获取{game}资讯")
    try:
        data = HoyoverseService.fetch_news(game)
        if data:
            return data
        raise HTTPException(status_code=404, detail="资讯未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取{game}资讯失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))