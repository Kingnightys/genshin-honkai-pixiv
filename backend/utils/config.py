from pydantic_settings import BaseSettings
from datetime import datetime

class Settings(BaseSettings):
    # 应用配置
    APP_TITLE: str = "Genshin/Honkai Star Rail API"
    APP_VERSION: str = "2.0.0"
    APP_DESCRIPTION: str = "整合Enka Network、Hakushin和HoYoverse API的原神/星穹铁道数据服务"
    
    # 服务器配置
    HOST: str = "192.168.8.49"
    PORT: int = 8000
    DEBUG: bool = True
    
    # API配置
    ENKA_API_URL: str = "https://api.enka.network"
    HAKUSHIN_API_URL: str = "https://api.hakush.in"
    HOYOVERSE_API_URL: str = "https://api.hoyoverse.com"
    
    # 请求配置
    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    REQUEST_DELAY: float = 0.5
    
    # 文件配置
    ASSETS_DIR: str = "assets"
    GENSHIN_DIR: str = "assets/genshin"
    STARRAIL_DIR: str = "assets/starrail"
    
    # 元素颜色映射
    ELEMENT_COLORS: dict = {
        '风': '#87CEEB', '火': '#FF6B6B', '水': '#4ECDC4', '冰': '#A8D8EA', 
        '雷': '#DDA0DD', '岩': '#CD853F', '草': '#90EE90',
        '物理': '#C0C0C0', '虚数': '#9370DB', '量子': '#FFD700', 
        '存护': '#FFA500', '巡猎': '#FF4500', '智识': '#1E90FF',
        '虚无': '#9400D3', '丰饶': '#32CD32', '同谐': '#FF69B4'
    }
    
    # 元素英文名映射
    ELEMENT_MAP: dict = {
        'Anemo': '风', 'Pyro': '火', 'Hydro': '水', 'Cryo': '冰', 
        'Electro': '雷', 'Geo': '岩', 'Dendro': '草',
        'Physical': '物理', 'Imaginary': '虚数', 'Quantum': '量子', 
        'Preservation': '存护', 'Hunt': '巡猎', 'Erudition': '智识',
        'Nihility': '虚无', 'Abundance': '丰饶', 'Harmony': '同谐'
    }
    
    @classmethod
    def get_current_time(cls) -> str:
        """获取当前时间"""
        return datetime.now().isoformat()

# 全局配置实例
settings = Settings()