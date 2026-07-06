from app.database.connection import SessionLocal
from app.repositories.prefeitura_repository import PrefeituraRepository
from app.services.discovery.discovery_engine import DiscoveryEngine
from app.services.prefeitura_service import PrefeituraService


def main():
    db = SessionLocal()

    try:
        prefeitura_repository = PrefeituraRepository(db)
        prefeitura_service = PrefeituraService(prefeitura_repository)
        discovery_engine = DiscoveryEngine()

        limite = 10

        prefeituras = prefeitura_service.listar_pendentes(limite)

        print("=" * 60)
        print("GV Radar - Descoberta de Prefeituras")
        print("=" * 60)
        print(f"Prefeituras pendentes selecionadas: {len(prefeituras)}")
        print()

        for index, prefeitura in enumerate(prefeituras, start=1):
            municipio = prefeitura.municipio

            print(f"[{index}/{len(prefeituras)}] {municipio.nome} - {municipio.uf}")

            resultado = discovery_engine.descobrir(
                municipio.nome,
                municipio.uf,
            )

            prefeitura_service.atualizar_descoberta(
                prefeitura,
                resultado,
            )

            if resultado.site_oficial:
                print(f"✅ Site encontrado: {resultado.site_oficial}")
            else:
                print(f"❌ Não encontrado: {resultado.observacao}")

            print("-" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()