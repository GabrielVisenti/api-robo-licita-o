"""Módulo responsável por listar municípios brasileiros.

Sprint 2:
- Busca a lista real de municípios na API pública do IBGE.
- Possui fallback local mínimo para a API continuar funcionando se o IBGE falhar.
"""

from functools import lru_cache
from typing import Dict, List
import requests

IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

FALLBACK_MUNICIPIOS: Dict[str, List[dict]] = {
    "PR": [
        {"nome": "Maringá", "codigo_ibge": "4115200"},
        {"nome": "Londrina", "codigo_ibge": "4113700"},
        {"nome": "Cascavel", "codigo_ibge": "4104808"},
        {"nome": "São Jorge do Ivaí", "codigo_ibge": "4125308"},
        {"nome": "Floraí", "codigo_ibge": "4107801"},
        {"nome": "Mandaguaçu", "codigo_ibge": "4114104"},
        {"nome": "Paiçandu", "codigo_ibge": "4117503"},
        {"nome": "Nova Esperança", "codigo_ibge": "4116901"},
        {"nome": "Ivatuba", "codigo_ibge": "4111605"},
    ],
    "MS": [
        {"nome": "Campo Grande", "codigo_ibge": "5002704"},
        {"nome": "Dourados", "codigo_ibge": "5003702"},
        {"nome": "Amambai", "codigo_ibge": "5000609"},
        {"nome": "Figueirão", "codigo_ibge": "5003900"},
    ],
    "SP": [
        {"nome": "São Paulo", "codigo_ibge": "3550308"},
        {"nome": "Campinas", "codigo_ibge": "3509502"},
        {"nome": "Ribeirão Preto", "codigo_ibge": "3543402"},
    ],
}

@lru_cache(maxsize=27)
def listar_municipios_detalhados_por_uf(uf: str) -> List[dict]:
    uf = uf.upper().strip()
    try:
        response = requests.get(IBGE_MUNICIPIOS_URL.format(uf=uf), timeout=20)
        response.raise_for_status()
        dados = response.json()
        municipios = [
            {
                "nome": item.get("nome", ""),
                "codigo_ibge": str(item.get("id", "")),
            }
            for item in dados
            if item.get("nome")
        ]
        return sorted(municipios, key=lambda x: x["nome"])
    except Exception:
        return FALLBACK_MUNICIPIOS.get(uf, [])

def listar_municipios_por_uf(uf: str) -> List[str]:
    return [m["nome"] for m in listar_municipios_detalhados_por_uf(uf)]
