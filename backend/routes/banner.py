from fastapi import APIRouter, HTTPException
from typing import Dict
from services.hakushin_service import HakushinService
from services.backup_service import BackupService
from utils.logger import logger

router = APIRouter(prefix="/banner", tags=["banner"])

@router.get("/genshin", response_model=Dict)
async def get_genshin_banner():
    """获取原神卡池信息"""
    logger.info("获取原神卡池信息")
    try:
        # 优先从Hakushin API获取
        data = HakushinService.fetch_genshin_banner()
        if data:
            return data
        
        # 备用数据
        logger.warning("Hakushin API失败，使用备用数据")
        return BackupService.get_genshin_banner_backup()
    except Exception as e:
        logger.error(f"获取原神卡池信息失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/starrail", response_model=Dict)
async def get_starrail_banner():
    """获取星穹铁道卡池信息"""
    logger.info("获取星穹铁道卡池信息")
    try:
        # 优先从Hakushin API获取
        data = HakushinService.fetch_starrail_banner()
        if data:
            return data
        
        # 备用数据
        logger.warning("Hakushin API失败，使用备用数据")
        return BackupService.get_starrail_banner_backup()
    except Exception as e:
        logger.error(f"获取星穹铁道卡池信息失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/beta/{game}", response_model=Dict)
async def get_beta_info(game: str):
    """获取测试服信息"""
    if game not in ["genshin", "starrail"]:
        raise HTTPException(status_code=400, detail="Invalid game. Use 'genshin' or 'starrail'.")
    
    logger.info(f"获取{game}测试服信息")
    try:
        data = HakushinService.fetch_beta_info(game)
        if data:
            return data
        raise HTTPException(status_code=404, detail="测试服信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取{game}测试服信息失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))