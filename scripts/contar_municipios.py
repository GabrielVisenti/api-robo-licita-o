from sqlalchemy import func

from app.database.connection import SessionLocal
from app.models.municipio import Municipio


def main():
    db = SessionLocal()

    try:
        total = db.query(func.count(Municipio.id)).scalar()

        print("=" * 50)
        print("GV Radar - Total de Municípios")
        print("=" * 50)
        print(f"Total de municípios cadastrados: {total}")

    finally:
        db.close()


if __name__ == "__main__":
    main()