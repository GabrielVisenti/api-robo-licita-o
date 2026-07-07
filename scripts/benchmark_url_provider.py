import sys
from time import perf_counter

from app.database.connection import SessionLocal
from app.repositories.prefeitura_repository import PrefeituraRepository
from app.services.discovery.discovery_engine import DiscoveryEngine
from app.services.prefeitura_service import PrefeituraService


def main():
    limite = 100

    if len(sys.argv) > 1:
        limite = int(sys.argv[1])

    db = SessionLocal()

    try:
        prefeitura_repository = PrefeituraRepository(db)
        prefeitura_service = PrefeituraService(prefeitura_repository)
        discovery_engine = DiscoveryEngine()

        prefeituras = prefeitura_service.listar(limite)

        encontrados = 0
        nao_encontrados = 0
        falhas = []
        resultados_por_municipio = []

        inicio_total = perf_counter()

        print("=" * 60)
        print("GV Radar - Benchmark UrlProvider")
        print("=" * 60)
        print(f"Municípios testados: {len(prefeituras)}")
        print()

        for prefeitura in prefeituras:
            municipio = prefeitura.municipio

            inicio_municipio = perf_counter()

            resultado = discovery_engine.descobrir(
                municipio.nome,
                municipio.uf,
            )

            tempo_municipio = perf_counter() - inicio_municipio

            encontrou = resultado.site_oficial is not None

            if encontrou:
                encontrados += 1
            else:
                nao_encontrados += 1
                falhas.append(f"{municipio.nome} - {municipio.uf}")

            resultados_por_municipio.append(
                {
                    "municipio": municipio.nome,
                    "uf": municipio.uf,
                    "encontrou": encontrou,
                    "tempo": tempo_municipio,
                    "site": resultado.site_oficial,
                }
            )

        tempo_total = perf_counter() - inicio_total
        total = len(prefeituras)
        taxa = (encontrados / total * 100) if total else 0
        tempo_medio = (tempo_total / total) if total else 0

        print("Resumo")
        print("-" * 60)
        print(f"Encontrados     : {encontrados}")
        print(f"Não encontrados : {nao_encontrados}")
        print(f"Taxa de sucesso : {taxa:.2f}%")
        print(f"Tempo total     : {tempo_total:.2f} segundos")
        print(f"Tempo médio     : {tempo_medio:.2f} segundos")
        print()

        print("Tempo por município")
        print("-" * 60)

        for item in sorted(
            resultados_por_municipio,
            key=lambda x: x["tempo"],
            reverse=True,
        ):
            status = "✅" if item["encontrou"] else "❌"
            print(
                f"{status} {item['municipio']} - {item['uf']} "
                f"| {item['tempo']:.2f}s"
            )

        print()

        if falhas:
            print("Municípios não encontrados:")
            for item in falhas:
                print(f"- {item}")

        print("=" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()