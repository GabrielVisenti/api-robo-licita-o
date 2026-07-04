from app.services.prefeitura_service import PrefeituraService


def main():
    service = PrefeituraService()

    municipio = "Maringá"
    uf = "PR"

    print("=" * 60)
    print("GV Radar - Teste Prefeitura Service")
    print("=" * 60)

    urls = service.gerar_urls_possiveis(municipio, uf)

    for url in urls:
        print(f"\nTestando: {url}")

        if service.verificar_url(url):
            print("✅ Site encontrado!")
        else:
            print("❌ Não encontrado")


if __name__ == "__main__":
    main()