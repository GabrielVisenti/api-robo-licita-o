from sqlalchemy import text

from app.database.connection import engine

print("=" * 50)
print("GV Radar - Teste de conexão com PostgreSQL")
print("=" * 50)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

        print()
        print("✅ Conexão realizada com sucesso!")
        print()
        print("Versão do PostgreSQL:")
        print(version)

except Exception as e:
    print()
    print("❌ Erro ao conectar ao banco:")
    print(e)