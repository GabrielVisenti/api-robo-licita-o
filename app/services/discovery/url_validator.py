from time import perf_counter

from app.domain.url_validation_result import UrlValidationResult
from app.services.discovery.http_client import HttpClient


class UrlValidator:

    def __init__(self):
        self.http_client = HttpClient()

    def validar(self, url: str) -> UrlValidationResult:
        inicio = perf_counter()

        response = self.http_client.get(url)

        tempo = perf_counter() - inicio

        if response is None:
            return UrlValidationResult(
                url=url,
                valido=False,
                tempo=tempo,
                erro="Sem resposta",
            )

        return UrlValidationResult(
            url=url,
            valido=response.status_code < 400,
            tempo=tempo,
            status_code=response.status_code,
            url_final=str(response.url),
        )