import requests
from typing import List, Dict, Optional
from utils.config import settings
from utils.logger import logger

class HoyoverseService:
    """HoYoverse Unified API服务"""
    
    @staticmethod
    def fetch_activities(game: str) -> Optional[List[Dict]]:
        """获取活动列表"""
        try:
            url = f"{settings.HOYOVERSE_API_URL}/api/{game}/activities"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"HoYoverse API获取{game}活动失败: {e}")
            return None
    
    @staticmethod
    def fetch_codes(game: str) -> Optional[List[Dict]]:
        """获取兑换码"""
        try:
            url = f"{settings.HOYOVERSE_API_URL}/api/{game}/codes"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"HoYoverse API获取{game}兑换码失败: {e}")
            return None
    
    @staticmethod
    def fetch_news(game: str) -> Optional[List[Dict]]:
        """获取最新资讯"""
        try:
            url = f"{settings.HOYOVERSE_API_URL}/api/{game}/news"
            response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"HoYoverse API获取{game}资讯失败: {e}")
            return None