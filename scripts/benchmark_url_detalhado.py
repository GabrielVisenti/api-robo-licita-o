from app.services.discovery.providers.url_provider import UrlProvider
from app.services.discovery.url_validator import UrlValidator


def testar_municipio(nome: str, uf: str):
    provider = UrlProvider()
    validator = UrlValidator()

    urls = provider.descobrir(nome, uf)

    print("=" * 60)
    print(f"Benchmark detalhado: {nome} - {uf}")
    print("=" * 60)

    for url in urls:
        resultado = validator.validar(url)

        status = "✅" if resultado.valido else "❌"

        print(f"{status} {resultado.url}")
        print(f"   Tempo: {resultado.tempo:.2f}s")
        print(f"   Status HTTP: {resultado.status_code}")
        print(f"   URL final: {resultado.url_final}")
        print(f"   Erro: {resultado.erro}")

        if resultado.valido:
            print()
            print(f"Site vencedor: {resultado.url}")
            break


def main():
    testar_municipio("Espigão D'Oeste", "RO")


if __name__ == "__main__":
    main()