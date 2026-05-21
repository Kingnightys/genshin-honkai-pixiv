from fastapi import APIRouter, HTTPException
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.hoyoverse_service import HoyoverseService
from utils.logger import logger

router = APIRouter(prefix="/activities", tags=["activities"])

@router.get("/", response_model=List[Dict])
async def get_activities(game: str = "genshin"):
    """获取活动列表"""
    if game not in ["genshin", "starrail"]:
        raise HTTPException(status_code=400, detail="Invalid game. Use 'genshin' or 'starrail'.")
    
    logger.info(f"获取{game}活动列表")
    try:
        data = HoyoverseService.fetch_activities(game)
        if data:
            return data
        raise HTTPException(status_code=404, detail="活动信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取{game}活动列表失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/codes", response_model=List[Dict])
async def get_codes(game: str = "genshin"):
    """获取兑换码"""
    if game not in ["genshin", "starrail"]:
        raise HTTPException(status_code=400, detail="Invalid game. Use 'genshin' or 'starrail'.")
    
    logger.info(f"获取{game}兑换码")
    try:
        data = HoyoverseService.fetch_codes(game)
        if data:
            return data
        raise HTTPException(status_code=404, detail="兑换码未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取{game}兑换码失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))