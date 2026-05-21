from fastapi import APIRouter, HTTPException
from typing import Dict, List
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.enka_service import EnkaService
from utils.logger import logger

router = APIRouter(prefix="/player", tags=["player"])

@router.get("/{uid}", response_model=Dict)
async def get_player_info(uid: str):
    """根据UID获取玩家信息"""
    logger.info(f"查询玩家信息: {uid}")
    try:
        # 使用Enka Network API获取玩家数据
        data = EnkaService.fetch_player_data(uid)
        if data:
            return data
        raise HTTPException(status_code=404, detail="玩家信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"查询玩家信息失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{uid}/characters", response_model=List[Dict])
async def get_player_characters(uid: str):
    """获取玩家拥有的角色列表"""
    logger.info(f"查询玩家角色: {uid}")
    try:
        data = EnkaService.fetch_player_data(uid)
        if data:
            return data.get('characters', [])
        raise HTTPException(status_code=404, detail="玩家角色信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"查询玩家角色失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{uid}/artifacts", response_model=Dict)
async def get_player_artifacts(uid: str):
    """获取玩家圣遗物配置"""
    logger.info(f"查询玩家圣遗物: {uid}")
    try:
        data = EnkaService.fetch_player_data(uid)
        if data:
            return data.get('artifacts', {})
        raise HTTPException(status_code=404, detail="玩家圣遗物信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"查询玩家圣遗物失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{uid}/build/{character_name}", response_model=Dict)
async def get_character_build(uid: str, character_name: str):
    """获取指定角色的练度和装备配置"""
    logger.info(f"查询角色配置: {uid} - {character_name}")
    try:
        data = EnkaService.fetch_player_data(uid)
        if data:
            characters = data.get('characters', [])
            for char in characters:
                if char.get('name') == character_name:
                    return char
            raise HTTPException(status_code=404, detail=f"角色 {character_name} 未找到")
        raise HTTPException(status_code=404, detail="玩家信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"查询角色配置失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{uid}/team-recommendation", response_model=List[Dict])
async def get_team_recommendation(uid: str):
    """获取配队推荐"""
    logger.info(f"获取配队推荐: {uid}")
    try:
        data = EnkaService.fetch_player_data(uid)
        if data:
            characters = data.get('characters', [])
            return generate_team_recommendation(characters)
        raise HTTPException(status_code=404, detail="玩家信息未找到")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取配队推荐失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def generate_team_recommendation(characters: List[Dict]) -> List[Dict]:
    """根据玩家角色生成配队推荐"""
    teams = []
    
    # 按元素分组
    element_groups = {
        '风': [], '火': [], '水': [], '冰': [], '雷': [], '岩': [], '草': []
    }
    
    for char in characters:
        element = char.get('element', '')
        if element in element_groups:
            element_groups[element].append(char)
    
    # 生成元素反应队伍
    # 燃烧队（火+草）
    if element_groups['火'] and element_groups['草']:
        teams.append({
            'name': '燃烧队',
            'description': '火元素与草元素触发燃烧反应',
            'characters': [
                element_groups['火'][0]['name'],
                element_groups['草'][0]['name'],
                '任意辅助',
                '任意治疗'
            ],
            'elements': ['火', '草']
        })
    
    # 激化队（雷+草）
    if element_groups['雷'] and element_groups['草']:
        teams.append({
            'name': '激化队',
            'description': '雷元素与草元素触发激化反应',
            'characters': [
                element_groups['雷'][0]['name'],
                element_groups['草'][0]['name'],
                '任意副C',
                '任意治疗'
            ],
            'elements': ['雷', '草']
        })
    
    # 蒸发队（火+水）
    if element_groups['火'] and element_groups['水']:
        teams.append({
            'name': '蒸发队',
            'description': '火元素与水元素触发蒸发反应',
            'characters': [
                element_groups['火'][0]['name'],
                element_groups['水'][0]['name'],
                '任意辅助',
                '任意治疗'
            ],
            'elements': ['火', '水']
        })
    
    # 融化队（火+冰）
    if element_groups['火'] and element_groups['冰']:
        teams.append({
            'name': '融化队',
            'description': '火元素与冰元素触发融化反应',
            'characters': [
                element_groups['火'][0]['name'],
                element_groups['冰'][0]['name'],
                '任意辅助',
                '任意治疗'
            ],
            'elements': ['火', '冰']
        })
    
    # 冻结队（水+冰）
    if element_groups['水'] and element_groups['冰']:
        teams.append({
            'name': '冻结队',
            'description': '水元素与冰元素触发冻结反应',
            'characters': [
                element_groups['水'][0]['name'],
                element_groups['冰'][0]['name'],
                '任意输出',
                '任意辅助'
            ],
            'elements': ['水', '冰']
        })
    
    # 感电队（雷+水）
    if element_groups['雷'] and element_groups['水']:
        teams.append({
            'name': '感电队',
            'description': '雷元素与水元素触发感电反应',
            'characters': [
                element_groups['雷'][0]['name'],
                element_groups['水'][0]['name'],
                '任意副C',
                '任意治疗'
            ],
            'elements': ['雷', '水']
        })
    
    return teams