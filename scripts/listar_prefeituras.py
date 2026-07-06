from app.database.connection import SessionLocal
from app.models.prefeitura import Prefeitura


def main():
    db = SessionLocal()

    try:
        prefeituras = db.query(Prefeitura).limit(20).all()

        print("=" * 60)
        print("GV Radar - Listagem de Prefeituras")
        print("=" * 60)

        for prefeitura in prefeituras:
            municipio = prefeitura.municipio

            print()
            print(f"{municipio.nome} - {municipio.uf}")
            print(f"Status: {prefeitura.status}")
            print(f"Site: {prefeitura.site_oficial or '-'}")
            print(f"Observação: {prefeitura.observacao or '-'}")
            print("-" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()