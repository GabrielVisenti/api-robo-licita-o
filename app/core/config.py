import os
from dataclasses import dataclass
from typing import List

@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    crawler_timeout_seconds: int = int(os.getenv("CRAWLER_TIMEOUT_SECONDS", "20"))
    crawler_max_workers: int = int(os.getenv("CRAWLER_MAX_WORKERS", "8"))

    @property
    def allowed_origins(self) -> List[str]:
        raw = os.getenv("ALLOWED_ORIGINS", "*")
        if raw.strip() == "*":
            return ["*"]
        return [item.strip() for item in raw.split(",") if item.strip()]

settings = Settings()
