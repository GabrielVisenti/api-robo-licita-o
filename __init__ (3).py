from datetime import date
from app.models.schemas import ResultadoMunicipio
from app.ia.classificador import classificar_relevancia

# Esta versão inicial retorna dados simulados para validar a integração com a Base44.
# A estrutura já está preparada para substituição gradual pelo crawler real.

def analisar_municipio(municipio: str, uf: str, data_diario: date) -> ResultadoMunicipio:
    nome = municipio.lower()

    if "maringá" in nome or "maringa" in nome:
        objeto = "Aquisição de equipamentos de informática"
        return ResultadoMunicipio(
            municipio=municipio,
            status="Licitação relevante encontrada",
            modalidade="Pregão Eletrônico",
            numero="10/2026",
            processo="",
            objeto=objeto,
            fonte="Diário Oficial Municipal",
            relevancia=classificar_relevancia(objeto),
            trecho_encontrado="Aviso de licitação para aquisição de equipamentos de informática.",
        )

    if "londrina" in nome:
        objeto = "Aquisição de toners e cartuchos"
        return ResultadoMunicipio(
            municipio=municipio,
            status="Licitação relevante encontrada",
            modalidade="Pregão Presencial",
            numero="58/2026",
            objeto=objeto,
            fonte="Diário Oficial Municipal",
            relevancia=classificar_relevancia(objeto),
            trecho_encontrado="Pregão presencial para aquisição de toners e cartuchos.",
        )

    if "cascavel" in nome:
        objeto = "Aquisição de impressoras e suprimentos de informática"
        return ResultadoMunicipio(
            municipio=municipio,
            status="Licitação relevante encontrada",
            modalidade="Dispensa Eletrônica",
            numero="22/2026",
            objeto=objeto,
            fonte="Diário Oficial Municipal",
            relevancia=classificar_relevancia(objeto),
            trecho_encontrado="Dispensa eletrônica para aquisição de impressoras e suprimentos.",
        )

    if "são jorge" in nome or "sao jorge" in nome:
        return ResultadoMunicipio(
            municipio=municipio,
            status="Site oficial indisponível",
            fonte="",
        )

    return ResultadoMunicipio(
        municipio=municipio,
        status="Nenhuma licitação referente aos segmentos monitorados",
        fonte="Diário Oficial Municipal",
    )
