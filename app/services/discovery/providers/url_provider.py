import unicodedata


class UrlProvider:

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