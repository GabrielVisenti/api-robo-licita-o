import unicodedata

from app.constants.url_patterns import URL_PATTERNS


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

    def descobrir(self, municipio_nome: str, uf: str) -> list[str]:
        nome = self.normalizar_nome(municipio_nome)
        uf = uf.lower()

        urls = {
            pattern.format(nome=nome, uf=uf)
            for pattern in URL_PATTERNS
        }

        return sorted(urls)