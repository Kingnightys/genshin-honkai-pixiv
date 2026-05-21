from .characters import router as characters_router
from .banner import router as banner_router
from .activities import router as activities_router
from .news import router as news_router
from .player import router as player_router
from .music import router as music_router
from .messages import router as messages_router
from .auth import router as auth_router

__all__ = [
    'characters_router',
    'banner_router',
    'activities_router',
    'news_router',
    'player_router',
    'music_router',
    'messages_router',
    'auth_router'
]