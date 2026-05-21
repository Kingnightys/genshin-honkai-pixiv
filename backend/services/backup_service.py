from typing import List, Dict

class BackupService:
    """备用数据服务"""
    
    @staticmethod
    def get_genshin_backup() -> List[Dict]:
        """获取原神备用角色数据"""
        return [
            {"name": "旅行者", "element": "风", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "安柏", "element": "火", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "芭芭拉", "element": "水", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "凯亚", "element": "冰", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "丽莎", "element": "雷", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "诺艾尔", "element": "岩", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "菲谢尔", "element": "雷", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "班尼特", "element": "火", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "香菱", "element": "火", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "北斗", "element": "雷", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "凝光", "element": "岩", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "琴", "element": "风", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "迪卢克", "element": "火", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "莫娜", "element": "水", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "可莉", "element": "火", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "温迪", "element": "风", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "钟离", "element": "岩", "version": "1.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "达达利亚", "element": "水", "version": "1.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "辛焱", "element": "火", "version": "1.1", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "甘雨", "element": "冰", "version": "1.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "阿贝多", "element": "岩", "version": "1.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "魈", "element": "风", "version": "1.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "胡桃", "element": "火", "version": "1.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "枫原万叶", "element": "风", "version": "1.6", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "神里绫华", "element": "冰", "version": "2.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "雷电将军", "element": "雷", "version": "2.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "宵宫", "element": "火", "version": "2.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "早柚", "element": "风", "version": "2.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "珊瑚宫心海", "element": "水", "version": "2.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "九条裟罗", "element": "雷", "version": "2.1", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "八重神子", "element": "雷", "version": "2.5", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "神里绫人", "element": "水", "version": "2.6", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "夜兰", "element": "水", "version": "2.7", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "久岐忍", "element": "雷", "version": "2.7", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "提纳里", "element": "草", "version": "3.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "柯莱", "element": "草", "version": "3.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "多莉", "element": "雷", "version": "3.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "纳西妲", "element": "草", "version": "3.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "莱依拉", "element": "冰", "version": "3.2", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "流浪者", "element": "风", "version": "3.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "珐露珊", "element": "风", "version": "3.3", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "艾尔海森", "element": "草", "version": "3.4", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "瑶瑶", "element": "草", "version": "3.4", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "迪希雅", "element": "火", "version": "3.5", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "米卡", "element": "冰", "version": "3.5", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "白术", "element": "草", "version": "3.6", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "卡维", "element": "草", "version": "3.6", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "林尼", "element": "火", "version": "4.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "琳妮特", "element": "风", "version": "4.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "菲米尼", "element": "水", "version": "4.1", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "纳维莱特", "element": "水", "version": "4.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "夏洛蒂", "element": "冰", "version": "4.2", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "芙宁娜", "element": "水", "version": "4.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "希诺宁", "element": "岩", "version": "4.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "阿蕾奇诺", "element": "火", "version": "4.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "闲云", "element": "风", "version": "4.4", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "嘉明", "element": "火", "version": "4.4", "rarity": 4, "image_url": "", "portrait_url": ""},
        ]
    
    @staticmethod
    def get_starrail_backup() -> List[Dict]:
        """获取星穹铁道备用角色数据"""
        return [
            {"name": "开拓者", "path": "物理", "element": "存护", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "三月七", "path": "冰", "element": "巡猎", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "丹恒", "path": "风", "element": "巡猎", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "姬子", "path": "火", "element": "智识", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "瓦尔特", "path": "虚数", "element": "虚无", "version": "1.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "杨叔", "path": "雷", "element": "存护", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "娜塔莎", "path": "冰", "element": "丰饶", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "希露瓦", "path": "雷", "element": "智识", "version": "1.0", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "布洛妮娅", "path": "风", "element": "同谐", "version": "1.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "杰帕德", "path": "冰", "element": "存护", "version": "1.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "佩拉", "path": "冰", "element": "虚无", "version": "1.1", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "希儿", "path": "风", "element": "巡猎", "version": "1.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "银狼", "path": "量子", "element": "虚无", "version": "1.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "罗刹", "path": "虚数", "element": "丰饶", "version": "1.2", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "景元", "path": "雷", "element": "智识", "version": "1.3", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "停云", "path": "雷", "element": "同谐", "version": "1.3", "rarity": 4, "image_url": "", "portrait_url": ""},
            {"name": "符玄", "path": "量子", "element": "存护", "version": "1.4", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "镜流", "path": "冰", "element": "巡猎", "version": "1.4", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "阮·梅", "path": "冰", "element": "同谐", "version": "2.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "黄泉", "path": "雷", "element": "巡猎", "version": "2.0", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "花火", "path": "风", "element": "虚无", "version": "2.1", "rarity": 5, "image_url": "", "portrait_url": ""},
            {"name": "缇宝", "path": "火", "element": "智识", "version": "2.3", "rarity": 5, "image_url": "", "portrait_url": ""},
        ]
    
    @staticmethod
    def get_genshin_banner_backup() -> Dict:
        """原神卡池备用数据"""
        return {
            "current_banner": "芙宁娜",
            "rate_up_characters": ["芙宁娜", "夏洛蒂"],
            "weapon_banner": "万世流涌大典",
            "next_banner": "希诺宁"
        }
    
    @staticmethod
    def get_starrail_banner_backup() -> Dict:
        """星穹铁道卡池备用数据"""
        return {
            "current_banner": "黄泉",
            "rate_up_characters": ["黄泉", "缇宝"],
            "weapon_banner": "专武UP",
            "next_banner": "花火"
        }