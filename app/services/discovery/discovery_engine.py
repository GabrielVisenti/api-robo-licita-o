from app.constants.status import PrefeituraStatus
from app.domain.discovery_result import DiscoveryResult
from app.services.discovery.providers.url_provider import UrlProvider
from app.services.discovery.url_validator import UrlValidator


class DiscoveryEngine:
    """
    Pipeline principal de descoberta do GV Radar.
    """

    def __init__(self):
        self.url_validator = UrlValidator()

        self.providers = [
            UrlProvider(),
        ]

    def descobrir(self, municipio_nome: str, uf: str) -> DiscoveryResult:

        for provider in self.providers:

            urls = provider.descobrir(municipio_nome, uf)

            for url in urls:
             if self.url_validator.validar(url):
                 return DiscoveryResult(
                site_oficial=url,
                status=PrefeituraStatus.CONCLUIDO,
                provider=provider.nome,
                observacao=f"Site encontrado via {provider.nome}.",
             )

        return DiscoveryResult(
            status=PrefeituraStatus.ERRO,
            observacao="Nenhuma estratégia encontrou um site válido.",
        )