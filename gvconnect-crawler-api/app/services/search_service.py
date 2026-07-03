from app.models.schemas import BuscarLicitacoesRequest, BuscarLicitacoesResponse, ResultadoMunicipio, MunicipiosDiscoveryResponse
from app.crawler.municipios import listar_municipios_detalhados_por_uf, listar_municipios_por_uf
from app.crawler.prefeitura import analisar_municipio, descobrir_sites_prefeituras

STATUS_COM_OPORTUNIDADE = "Licitação relevante encontrada"


def executar_discovery_municipios(uf: str) -> MunicipiosDiscoveryResponse:
    uf = uf.upper().strip()
    municipios = listar_municipios_detalhados_por_uf(uf)
    resultados = descobrir_sites_prefeituras(municipios, uf)
    encontrados = sum(1 for r in resultados if r.site_prefeitura)
    return MunicipiosDiscoveryResponse(
        uf=uf,
        total_municipios=len(resultados),
        encontrados=encontrados,
        nao_encontrados=len(resultados) - encontrados,
        resultados=resultados,
    )


def executar_busca_licitacoes(payload: BuscarLicitacoesRequest) -> BuscarLicitacoesResponse:
    # Sprint 2: usamos descoberta paralela de sites oficiais para todos os municípios.
    # Na Sprint 3, a partir de site_prefeitura, vamos localizar a página do Diário Oficial.
    municipios_detalhados = listar_municipios_detalhados_por_uf(payload.uf)
    descobertas = descobrir_sites_prefeituras(municipios_detalhados, payload.uf)

    resultados: list[ResultadoMunicipio] = []
    for descoberta in descobertas:
        if descoberta.site_prefeitura:
            resultados.append(
                ResultadoMunicipio(
                    municipio=descoberta.municipio,
                    status="Site oficial encontrado; Diário Oficial ainda não analisado",
                    fonte="Site da Prefeitura",
                    site_prefeitura=descoberta.site_prefeitura,
                    trecho_encontrado=f"Site localizado automaticamente: {descoberta.site_prefeitura}",
                )
            )
        else:
            resultados.append(
                ResultadoMunicipio(
                    municipio=descoberta.municipio,
                    status="Site oficial não localizado automaticamente",
                    fonte="",
                    trecho_encontrado="A Sprint 2 tentou padrões oficiais de domínio, mas não confirmou o site.",
                )
            )

    municipios_com_oportunidade = sum(1 for r in resultados if r.status == STATUS_COM_OPORTUNIDADE)
    municipios_com_erro = sum(
        1
        for r in resultados
        if "erro" in r.status.lower()
        or "indisponível" in r.status.lower()
        or "não localizado" in r.status.lower()
    )
    municipios_sem_oportunidade = len(resultados) - municipios_com_oportunidade - municipios_com_erro
    total_licitacoes_encontradas = municipios_com_oportunidade

    return BuscarLicitacoesResponse(
        estado=payload.estado,
        uf=payload.uf.upper(),
        data_diario=str(payload.data_diario),
        total_municipios=len(resultados),
        municipios_com_oportunidade=municipios_com_oportunidade,
        municipios_sem_oportunidade=municipios_sem_oportunidade,
        municipios_com_erro=municipios_com_erro,
        total_licitacoes_encontradas=total_licitacoes_encontradas,
        resultados=resultados,
    )
