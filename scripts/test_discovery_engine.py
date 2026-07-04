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

        site = engine.descobrir_site_prefeitura(nome, uf)

        if site:
            print(f"✅ Site encontrado: {site}")
        else:
            print("❌ Site não encontrado")


if __name__ == "__main__":
    main()