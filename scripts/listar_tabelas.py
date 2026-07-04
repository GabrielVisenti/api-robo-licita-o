from sqlalchemy import inspect

from app.database.connection import engine


def main():
    inspector = inspect(engine)

    print("=" * 50)
    print("GV Radar - Tabelas do Banco")
    print("=" * 50)

    for tabela in inspector.get_table_names():
        print(f"• {tabela}")


if __name__ == "__main__":
    main()