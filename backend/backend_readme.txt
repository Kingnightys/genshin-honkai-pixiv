backend/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── logger.py
├── models/
│   ├── __init__.py
│   ├── character.py
│   └── banner.py
├── services/
│   ├── __init__.py
│   ├── enka_service.py      # 增强版，支持玩家数据查询
│   ├── hakushin_service.py
│   ├── hoyoverse_service.py
│   └── backup_service.py
└── routes/
    ├── __init__.py
    ├── characters.py
    ├── banner.py
    ├── activities.py
    ├── news.py
    └── player.py            # 新增：UID查询路由
