import httpx


class PrefeituraService:

    def gerar_urls_possiveis(self, nome_municipio: str, uf: str):
        nome_normalizado = (
            nome_municipio.lower()
            .replace(" ", "")
            .replace("ã", "a")
            .replace("á", "a")
            .replace("à", "a")
            .replace("â", "a")
            .replace("é", "e")
            .replace("ê", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ô", "o")
            .replace("õ", "o")
            .replace("ú", "u")
            .replace("ç", "c")
        )

        uf = uf.lower()

        return [
            f"https://www.{nome_normalizado}.{uf}.gov.br",
            f"https://{nome_normalizado}.{uf}.gov.br",
            f"https://www.prefeitura{nome_normalizado}.{uf}.gov.br",
            f"https://prefeitura{nome_normalizado}.{uf}.gov.br",
        ]

    def verificar_url(self, url: str) -> bool:
        try:
            response = httpx.get(url, timeout=10, follow_redirects=True)
            return response.status_code < 400
        except Exception:
            return False