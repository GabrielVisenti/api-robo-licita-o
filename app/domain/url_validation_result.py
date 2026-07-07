from dataclasses import dataclass


@dataclass(slots=True)
class UrlValidationResult:
    url: str
    valido: bool
    tempo: float
    status_code: int | None = None
    erro: str | None = None
    url_final: str | None = None