from fastapi import APIRouter, HTTPException
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.enka_service import EnkaService
from services.backup_service import BackupService
from utils.logger import logger

router = APIRouter(prefix="/characters", tags=["characters"])

@router.get("/genshin", response_model=List[Dict])
async def get_genshin_characters():
    """获取原神角色数据"""
    logger.info("获取原神角色数据")
    try:
        # 优先从Enka API获取
        data = EnkaService.fetch_genshin_characters()
        if data:
            return data
        
        # 备用数据
        logger.warning("Enka API失败，使用备用数据")
        return BackupService.get_genshin_backup()
    except Exception as e:
        logger.error(f"获取原神角色数据失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/starrail", response_model=List[Dict])
async def get_starrail_characters():
    """获取星穹铁道角色数据"""
    logger.info("获取星穹铁道角色数据")
    try:
        # 优先从Enka API获取
        data = EnkaService.fetch_starrail_characters()
        if data:
            return data
        
        # 备用数据
        logger.warning("Enka API失败，使用备用数据")
        return BackupService.get_starrail_backup()
    except Exception as e:
        logger.error(f"获取星穹铁道角色数据失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{game}", response_model=List[Dict])
async def get_characters(game: str):
    """获取指定游戏的角色数据"""
    if game not in ["genshin", "starrail"]:
        raise HTTPException(status_code=400, detail="Invalid game. Use 'genshin' or 'starrail'.")
    
    if game == "genshin":
        return await get_genshin_characters()
    else:
        return await get_starrail_characters()