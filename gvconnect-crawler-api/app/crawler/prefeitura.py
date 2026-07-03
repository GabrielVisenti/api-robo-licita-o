"""Descoberta de sites oficiais de prefeituras.

Sprint 2:
- Gera candidatos prováveis de domínio oficial.
- Testa HTTP/HTTPS com timeout curto.
- Valida se a página parece ser prefeitura municipal.

Importante: esta etapa NÃO lê Diário Oficial ainda. Ela só descobre o site da prefeitura.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from app.models.schemas import MunicipioDescoberto, ResultadoMunicipio
from app.utils.text import dominio_municipio, slug_municipio, remover_acentos

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; GVConnectCrawler/1.0; +https://gvconnect-crawler-api.onrender.com)"
}

PALAVRAS_VALIDACAO = [
    "prefeitura",
    "municipio",
    "município",
    "portal oficial",
    "governo municipal",
]


def gerar_candidatos_site_prefeitura(municipio: str, uf: str) -> List[str]:
    uf = uf.lower().strip()
    slug = slug_municipio(municipio)
    dominio = dominio_municipio(municipio)

    candidatos = [
        f"https://www.{dominio}.{uf}.gov.br",
        f"https://{dominio}.{uf}.gov.br",
        f"http://www.{dominio}.{uf}.gov.br",
        f"http://{dominio}.{uf}.gov.br",
        f"https://www.{slug}.{uf}.gov.br",
        f"https://{slug}.{uf}.gov.br",
        f"https://www.prefeitura{dominio}.{uf}.gov.br",
        f"https://prefeitura{dominio}.{uf}.gov.br",
        f"https://www.{dominio}.pr.gov.br" if uf == "pr" else "",
        f"https://www.{dominio}.sp.gov.br" if uf == "sp" else "",
        f"https://www.{dominio}.ms.gov.br" if uf == "ms" else "",
    ]

    vistos = set()
    limpos = []
    for url in candidatos:
        if url and url not in vistos:
            vistos.add(url)
            limpos.append(url)
    return limpos


def _pagina_parece_prefeitura(html: str, municipio: str) -> bool:
    texto = BeautifulSoup(html, "html.parser").get_text(" ", strip=True).lower()
    municipio_sem_acento = remover_acentos(municipio).lower()
    texto_sem_acento = remover_acentos(texto)

    tem_municipio = municipio_sem_acento in texto_sem_acento
    tem_palavra_oficial = any(p in texto for p in PALAVRAS_VALIDACAO)

    return tem_municipio and tem_palavra_oficial


def testar_url_prefeitura(url: str, municipio: str) -> Optional[str]:
    try:
        response = requests.get(url, headers=HEADERS, timeout=8, allow_redirects=True)
        if response.status_code >= 400:
            return None
        content_type = response.headers.get("content-type", "").lower()
        if "text/html" not in content_type and "application/xhtml" not in content_type:
            return None
        if _pagina_parece_prefeitura(response.text[:200_000], municipio):
            return str(response.url).rstrip("/")
        return None
    except Exception:
        return None


def descobrir_site_prefeitura(municipio: str, uf: str) -> MunicipioDescoberto:
    candidatos = gerar_candidatos_site_prefeitura(municipio, uf)
    for url in candidatos:
        encontrado = testar_url_prefeitura(url, municipio)
        if encontrado:
            return MunicipioDescoberto(
                municipio=municipio,
                uf=uf.upper(),
                site_prefeitura=encontrado,
                status="Site oficial encontrado",
                candidatos_testados=candidatos,
            )

    return MunicipioDescoberto(
        municipio=municipio,
        uf=uf.upper(),
        site_prefeitura="",
        status="Site oficial não localizado automaticamente",
        candidatos_testados=candidatos,
    )


def descobrir_sites_prefeituras(municipios: List[dict], uf: str, max_workers: int = 12) -> List[MunicipioDescoberto]:
    resultados: List[MunicipioDescoberto] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(descobrir_site_prefeitura, item["nome"], uf): item
            for item in municipios
        }
        for future in as_completed(futures):
            item = futures[future]
            try:
                resultado = future.result()
                resultado.codigo_ibge = item.get("codigo_ibge", "")
                resultados.append(resultado)
            except Exception:
                resultados.append(
                    MunicipioDescoberto(
                        municipio=item["nome"],
                        uf=uf.upper(),
                        codigo_ibge=item.get("codigo_ibge", ""),
                        status="Erro ao tentar localizar site oficial",
                    )
                )

    return sorted(resultados, key=lambda x: x.municipio)


def analisar_municipio(municipio: str, uf: str, data_diario: date) -> ResultadoMunicipio:
    """Integração provisória da Sprint 2 com o relatório da Base44.

    Em vez de retornar dados simulados de licitação, agora retornamos o status real
    da descoberta do site. Na Sprint 3, este método passará a descobrir e ler o
    Diário Oficial da data informada.
    """
    descoberta = descobrir_site_prefeitura(municipio, uf)

    if descoberta.site_prefeitura:
        return ResultadoMunicipio(
            municipio=municipio,
            status="Site oficial encontrado; Diário Oficial ainda não analisado",
            fonte="Site da Prefeitura",
            site_prefeitura=descoberta.site_prefeitura,
            trecho_encontrado=f"Site localizado automaticamente: {descoberta.site_prefeitura}",
        )

    return ResultadoMunicipio(
        municipio=municipio,
        status="Site oficial não localizado automaticamente",
        fonte="",
        trecho_encontrado="A Sprint 2 tentou padrões oficiais de domínio, mas não confirmou o site.",
    )
