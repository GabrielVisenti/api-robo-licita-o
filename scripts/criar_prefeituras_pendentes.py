from app.database.connection import SessionLocal
from app.models.municipio import Municipio
from app.repositories.prefeitura_repository import PrefeituraRepository
from app.services.prefeitura_service import PrefeituraService


def main():
    db = SessionLocal()

    try:
        prefeitura_repository = PrefeituraRepository(db)
        prefeitura_service = PrefeituraService(prefeitura_repository)

        municipios = db.query(Municipio).limit(10).all()

        print("=" * 60)
        print("GV Radar - Criando Prefeituras Pendentes")
        print("=" * 60)

        criadas = 0
        ignoradas = 0

        for municipio in municipios:

            existente = prefeitura_service.buscar_por_municipio_id(
                municipio.id
            )

            if existente:
                ignoradas += 1
                continue

            prefeitura_service.criar_prefeitura(municipio.id)
            criadas += 1

            print(f"✓ {municipio.nome}")

        print()
        print("=" * 60)
        print(f"Criadas   : {criadas}")
        print(f"Ignoradas : {ignoradas}")
        print("=" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()