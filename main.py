from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title="GV CONNECT Crawler API",
    description="API externa para o Radar de Licitações Municipais — GV CONNECT.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "GV CONNECT Crawler API",
        "docs": "/docs",
        "health": "/api/health",
    }
