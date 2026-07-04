import os
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./gv_radar.db")
    crawler_timeout_seconds: int = int(os.getenv("CRAWLER_TIMEOUT_SECONDS", "20"))
    crawler_max_workers: int = int(os.getenv("CRAWLER_MAX_WORKERS", "8"))

    @property
    def allowed_origins(self) -> List[str]:
        raw = os.getenv("ALLOWED_ORIGINS", "*")
        if raw.strip() == "*":
            return ["*"]
        return [item.strip() for item in raw.split(",") if item.strip()]

settings = Settings()
