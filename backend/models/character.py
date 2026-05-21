from pydantic import BaseModel, Field
from typing import Optional

class Character(BaseModel):
    """角色数据模型"""
    name: str = Field(..., description="角色名称")
    element: str = Field(..., description="元素属性")
    path: Optional[str] = Field(None, description="星穹铁道角色命途")
    rarity: int = Field(..., description="稀有度(4/5)")
    version: str = Field(..., description="实装版本")
    local_path: str = Field(..., description="本地图片路径")
    description: Optional[str] = Field(None, description="角色描述")
    image_url: Optional[str] = Field(None, description="图片URL")
    portrait_url: Optional[str] = Field(None, description="立绘URL")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "芙宁娜",
                "element": "水",
                "rarity": 5,
                "version": "4.2",
                "local_path": "/assets/genshin/芙宁娜.png",
                "description": "枫丹的水之神"
            }
        }