from sqlalchemy import func

from app.database.connection import SessionLocal
from app.models.prefeitura import Prefeitura


def main():
    db = SessionLocal()

    try:
        total = db.query(func.count(Prefeitura.id)).scalar()

        print("=" * 50)
        print("GV Radar - Total de Prefeituras")
        print("=" * 50)
        print(f"Total de prefeituras cadastradas: {total}")

    finally:
        db.close()


if __name__ == "__main__":
    main()