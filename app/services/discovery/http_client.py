import httpx


class HttpClient:
    """
    Cliente HTTP centralizado do GV Radar.

    Todas as requisições HTTP do sistema deverão passar por esta classe.
    """

    def __init__(self):
        self.client = httpx.Client(
            timeout=20,
            follow_redirects=True,
            headers={
                "User-Agent": (
                    "GVRadar/1.0 "
                    "(https://github.com/GabrielVisenti/api-robo-licita-o)"
                )
            },
        )

    def get(self, url: str):
        try:
            response = self.client.get(url)

            return response

        except Exception:
            return None