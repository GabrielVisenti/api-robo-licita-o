import unicodedata

from app.constants.status import PrefeituraStatus
from app.models.discovery_result import DiscoveryResult


class UrlProvider:

    nome = "UrlProvider"

    def normalizar_nome(self, nome: str) -> str:
        texto = nome.lower().strip()

        texto = unicodedata.normalize("NFKD", texto)
        texto = "".join(c for c in texto if not unicodedata.combining(c))

        texto = texto.replace("'", "")
        texto = texto.replace("-", "")
        texto = texto.replace(" ", "")

        return texto

    def gerar_urls_prefeitura(self, municipio_nome: str, uf: str):
        nome = self.normalizar_nome(municipio_nome)
        uf = uf.lower()

        return [
            f"https://www.{nome}.{uf}.gov.br",
            f"https://{nome}.{uf}.gov.br",
            f"https://www.prefeitura{nome}.{uf}.gov.br",
            f"https://prefeitura{nome}.{uf}.gov.br",
        ]

    def descobrir(self, municipio_nome: str, uf: str, verificar_site):
        urls = self.gerar_urls_prefeitura(municipio_nome, uf)

        for url in urls:
            if verificar_site(url):
                return DiscoveryResult(
                    site_oficial=url,
                    status=PrefeituraStatus.CONCLUIDO,
                    provider=self.nome,
                    observacao="Site encontrado por padrão de URL.",
                )

        return DiscoveryResult(
            status=PrefeituraStatus.ERRO,
            provider=self.nome,
            observacao="Nenhuma URL padrão respondeu com sucesso.",
        )