from app.database.connection import SessionLocal
from app.repositories.municipio_repository import MunicipioRepository
from app.services.importers.municipio_importer import MunicipioImporter
from app.services.municipio_service import MunicipioService


def main():
    db = SessionLocal()

    try:
        municipio_service = MunicipioService()
        municipio_repository = MunicipioRepository(db)

        importer = MunicipioImporter(
            municipio_service=municipio_service,
            municipio_repository=municipio_repository,
        )

        importer.executar()

    finally:
        db.close()


if __name__ == "__main__":
    main()