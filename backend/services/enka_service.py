import requests
from typing import List, Dict, Optional
from utils.config import settings
from utils.logger import logger

class EnkaService:
    """Enka Network API服务"""
    
    @staticmethod
    def fetch_player_data(uid: str) -> Optional[Dict]:
        """获取玩家展示柜数据"""
        try:
            # 检测游戏类型（原神UID为9位数字，星穹铁道为10位）
            game = 'starrail' if len(uid) == 10 else 'genshin'
            url = f"{settings.ENKA_API_URL}/api/uid/{game}/{uid}"
            
            headers = {
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=settings.REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            # 解析玩家信息
            return {
                'uid': uid,
                'game': game,
                'nickname': data.get('playerInfo', {}).get('nickname', ''),
                'level': data.get('playerInfo', {}).get('level', 0),
                'characters': EnkaService._parse_characters(data),
                'artifacts': EnkaService._parse_artifacts(data),
                'weapons': EnkaService._parse_weapons(data)
            }
        except Exception as e:
            logger.error(f"Enka API获取玩家数据失败: {e}")
            return None
    
    @staticmethod
    def _parse_characters(data: Dict) -> List[Dict]:
        """解析角色数据"""
        characters = []
        for char in data.get('avatarInfoList', []):
            character = {
                'name': char.get('avatarName', ''),
                'element': settings.ELEMENT_MAP.get(char.get('element', ''), ''),
                'level': char.get('level', 0),
                'constellation': char.get('constellation', 0),
                'weapon': EnkaService._parse_weapon(char),
                'artifacts': EnkaService._parse_character_artifacts(char),
                'stats': EnkaService._parse_stats(char)
            }
            characters.append(character)
        return characters
    
    @staticmethod
    def _parse_weapon(char_data: Dict) -> Dict:
        """解析武器信息"""
        weapon = char_data.get('weapon', {})
        return {
            'name': weapon.get('name', ''),
            'rarity': weapon.get('rarity', 0),
            'level': weapon.get('level', 0),
            'refinement': weapon.get('refinement', 1)
        }
    
    @staticmethod
    def _parse_character_artifacts(char_data: Dict) -> List[Dict]:
        """解析角色圣遗物"""
        artifacts = []
        for artifact in char_data.get('reliquaryList', []):
            artifacts.append({
                'name': artifact.get('name', ''),
                'set': artifact.get('setName', ''),
                'rarity': artifact.get('rarity', 0),
                'level': artifact.get('level', 0),
                'main_stat': artifact.get('mainStat', {}).get('name', ''),
                'sub_stats': artifact.get('subStats', [])
            })
        return artifacts
    
    @staticmethod
    def _parse_stats(char_data: Dict) -> Dict:
        """解析角色属性"""
        stats = {}
        for stat in char_data.get('fightPropMap', {}):
            stats[stat] = char_data['fightPropMap'][stat]
        return stats
    
    @staticmethod
    def _parse_artifacts(data: Dict) -> Dict:
        """解析所有圣遗物"""
        all_artifacts = {}
        for char in data.get('avatarInfoList', []):
            char_name = char.get('avatarName', '')
            all_artifacts[char_name] = EnkaService._parse_character_artifacts(char)
        return all_artifacts
    
    @staticmethod
    def _parse_weapons(data: Dict) -> Dict:
        """解析所有武器"""
        all_weapons = {}
        for char in data.get('avatarInfoList', []):
            char_name = char.get('avatarName', '')
            all_weapons[char_name] = EnkaService._parse_weapon(char)
        return all_weapons
    
    # ... 原有方法保持不变 ...