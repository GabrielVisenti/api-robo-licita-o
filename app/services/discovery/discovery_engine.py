from app.models.discovery_result import DiscoveryResult
from app.services.discovery.http_client import HttpClient
from app.services.discovery.providers.url_provider import UrlProvider


class DiscoveryEngine:
    """
    Pipeline principal de descoberta do GV Radar.
    """

    def __init__(self):
        self.http_client = HttpClient()

        self.providers = [
            UrlProvider(),
        ]

    def verificar_site(self, url: str) -> bool:
        response = self.http_client.get(url)

        if response is None:
            return False

        return response.status_code < 400

    def descobrir(self, municipio_nome: str, uf: str) -> DiscoveryResult:

        for provider in self.providers:

            resultado = provider.descobrir(
                municipio_nome,
                uf,
                self.verificar_site,
            )

            if resultado.site_oficial:
                return resultado

        return DiscoveryResult()