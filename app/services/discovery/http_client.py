import httpx


class HttpClient:
    """
    Cliente HTTP centralizado do GV Radar.
    """

    def __init__(self):
        timeout = httpx.Timeout(
            connect=3.0,
            read=5.0,
            write=5.0,
            pool=3.0,
        )

        self.client = httpx.Client(
            timeout=timeout,
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
            return self.client.get(url)

        except httpx.TimeoutException:
            return None

        except httpx.ConnectError:
            return None

        except httpx.HTTPError:
            return None

    def head(self, url: str):
        try:
            return self.client.head(url)

        except httpx.TimeoutException:
            return None

        except httpx.ConnectError:
            return None

        except httpx.HTTPError:
            return None

    def close(self):
        self.client.close()