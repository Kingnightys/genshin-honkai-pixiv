import requests
from typing import Dict, Optional
from utils.config import settings
from utils.logger import logger

class HakushinService:
    """Hakushin API服务 - 测试服数据"""
    
    @staticmethod
    def fetch_genshin_banner() -> Optional[Dict]:
        """获取原神卡池信息"""
        try:
            url = f"{settings.HAKUSHIN_API_URL}/genshin/banner"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            return {
                "current_banner": data.get("current", {}).get("character", "未知"),
                "rate_up_characters": data.get("current", {}).get("rateUp", []),
                "weapon_banner": data.get("current", {}).get("weapon", "未知"),
                "next_banner": data.get("next", {}).get("character", "未知"),
                "banner_end_time": data.get("current", {}).get("endTime")
            }
        except Exception as e:
            logger.error(f"Hakushin API获取原神卡池失败: {e}")
            return None
    
    @staticmethod
    def fetch_starrail_banner() -> Optional[Dict]:
        """获取星穹铁道卡池信息"""
        try:
            url = f"{settings.HAKUSHIN_API_URL}/starrail/banner"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            return {
                "current_banner": data.get("current", {}).get("character", "未知"),
                "rate_up_characters": data.get("current", {}).get("rateUp", []),
                "weapon_banner": data.get("current", {}).get("lightcone", "未知"),
                "next_banner": data.get("next", {}).get("character", "未知"),
                "banner_end_time": data.get("current", {}).get("endTime")
            }
        except Exception as e:
            logger.error(f"Hakushin API获取星穹铁道卡池失败: {e}")
            return None
    
    @staticmethod
    def fetch_beta_info(game: str) -> Optional[Dict]:
        """获取测试服信息"""
        try:
            url = f"{settings.HAKUSHIN_API_URL}/{game}/beta"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Hakushin API获取{game}测试服信息失败: {e}")
            return None