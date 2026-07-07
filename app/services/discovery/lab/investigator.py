from app.domain.url_validation_result import UrlValidationResult
from app.services.discovery.providers.url_provider import UrlProvider
from app.services.discovery.url_validator import UrlValidator


class MunicipioInvestigator:

    def __init__(self):
        self.url_provider = UrlProvider()
        self.url_validator = UrlValidator()

    def investigar(self, nome: str, uf: str) -> list[UrlValidationResult]:
        urls = self.url_provider.descobrir(nome, uf)

        resultados: list[UrlValidationResult] = []

        for url in urls:
            resultado = self.url_validator.validar(url)
            resultados.append(resultado)

        return resultados