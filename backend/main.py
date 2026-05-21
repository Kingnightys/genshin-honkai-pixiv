from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import characters, banner, activities, news, player, music, messages, auth

app = FastAPI(title="Genshin/Honkai API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(characters.router, prefix="/api")
app.include_router(banner.router, prefix="/api")
app.include_router(activities.router, prefix="/api")
app.include_router(news.router, prefix="/api")
app.include_router(player.router, prefix="/api")
app.include_router(music.router, prefix="/api")
app.include_router(messages.router, prefix="/api")
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "API is running"}
