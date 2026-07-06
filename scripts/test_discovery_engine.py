from app.services.discovery.discovery_engine import DiscoveryEngine


def main():
    engine = DiscoveryEngine()

    municipios = [
        ("Maringá", "PR"),
        ("São Jorge do Ivaí", "PR"),
        ("Guajará-Mirim", "RO"),
    ]

    print("=" * 60)
    print("GV Radar - Teste Discovery Engine")
    print("=" * 60)

    for nome, uf in municipios:
        print()
        print(f"Município: {nome} - {uf}")

        resultado = engine.descobrir(nome, uf)

        if resultado.site_oficial:
            print(f"✅ Site encontrado: {resultado.site_oficial}")
            print(f"Provider: {resultado.provider}")
            print(f"Status: {resultado.status}")
        else:
            print("❌ Site não encontrado")
            print(f"Status: {resultado.status}")
            print(f"Observação: {resultado.observacao}")


if __name__ == "__main__":
    main()