from app.models.schemas import BuscarLicitacoesRequest, BuscarLicitacoesResponse, ResultadoMunicipio
from app.crawler.municipios import listar_municipios_por_uf
from app.crawler.prefeitura import analisar_municipio

STATUS_COM_OPORTUNIDADE = "Licitação relevante encontrada"

def executar_busca_licitacoes(payload: BuscarLicitacoesRequest) -> BuscarLicitacoesResponse:
    municipios = listar_municipios_por_uf(payload.uf)
    resultados: list[ResultadoMunicipio] = []

    for municipio in municipios:
        resultado = analisar_municipio(
            municipio=municipio,
            uf=payload.uf,
            data_diario=payload.data_diario,
        )
        resultados.append(resultado)

    municipios_com_oportunidade = sum(1 for r in resultados if r.status == STATUS_COM_OPORTUNIDADE)
    municipios_com_erro = sum(1 for r in resultados if "erro" in r.status.lower() or "indisponível" in r.status.lower() or "não localizado" in r.status.lower())
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
