# Primeira versão com lista reduzida para testes rápidos.
# Depois podemos trocar por base completa do IBGE por UF.

MUNICIPIOS_POR_UF = {
    "PR": [
        "Maringá",
        "Londrina",
        "Cascavel",
        "São Jorge do Ivaí",
        "Floraí",
        "Mandaguaçu",
        "Paiçandu",
        "Nova Esperança",
        "Ivatuba",
    ],
    "MS": [
        "Campo Grande",
        "Dourados",
        "Amambai",
        "Figueirão",
    ],
    "SP": [
        "São Paulo",
        "Campinas",
        "Ribeirão Preto",
    ],
}

def listar_municipios_por_uf(uf: str) -> list[str]:
    uf = uf.upper().strip()
    return MUNICIPIOS_POR_UF.get(uf, [])
