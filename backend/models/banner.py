from pydantic import BaseModel, Field
from typing import List, Optional

class BannerData(BaseModel):
    """卡池数据模型"""
    current_banner: str = Field(..., description="当前UP角色")
    rate_up_characters: List[str] = Field(..., description="UP角色列表")
    weapon_banner: str = Field(..., description="武器/光锥卡池")
    next_banner: Optional[str] = Field(None, description="下一期UP角色")
    banner_end_time: Optional[str] = Field(None, description="卡池结束时间")
    
    class Config:
        schema_extra = {
            "example": {
                "current_banner": "芙宁娜",
                "rate_up_characters": ["芙宁娜", "夏洛蒂"],
                "weapon_banner": "万世流涌大典",
                "next_banner": "希诺宁"
            }
        }