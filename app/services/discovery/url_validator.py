from app.services.discovery.http_client import HttpClient


class UrlValidator:

    def __init__(self):
        self.http_client = HttpClient()

    def validar(self, url: str) -> bool:
        response = self.http_client.get(url)

        if response is None:
            return False

        return response.status_code < 400