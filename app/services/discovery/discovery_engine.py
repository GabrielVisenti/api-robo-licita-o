from app.services.discovery.http_client import HttpClient
from app.services.discovery.providers.url_provider import UrlProvider


class DiscoveryEngine:
    """
    Motor central de descoberta do GV Radar.
    """

    def __init__(self):
        self.http_client = HttpClient()
        self.url_provider = UrlProvider()

    def verificar_site(self, url: str) -> bool:
        response = self.http_client.get(url)

        if response is None:
            return False

        return response.status_code < 400

    def descobrir_site_prefeitura(self, municipio_nome: str, uf: str):
        urls = self.url_provider.gerar_urls_prefeitura(municipio_nome, uf)

        for url in urls:
            if self.verificar_site(url):
                return url

        return None

    def descobrir_diario_oficial(self, site_prefeitura: str):
        return None

    def descobrir_portal_licitacoes(self, site_prefeitura: str):
        return None