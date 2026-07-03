from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class BuscarLicitacoesRequest(BaseModel):
    estado: str = Field(..., examples=["Paraná"])
    uf: str = Field(..., examples=["PR"])
    data_diario: date = Field(..., examples=["2026-07-03"])

class ResultadoMunicipio(BaseModel):
    municipio: str
    status: str
    modalidade: str = ""
    numero: str = ""
    processo: str = ""
    objeto: str = ""
    fonte: str = ""
    relevancia: str = ""
    trecho_encontrado: str = ""
    site_prefeitura: str = ""
    diario_url: str = ""

class BuscarLicitacoesResponse(BaseModel):
    estado: str
    uf: str
    data_diario: str
    total_municipios: int
    municipios_com_oportunidade: int
    municipios_sem_oportunidade: int
    municipios_com_erro: int
    total_licitacoes_encontradas: int
    resultados: List[ResultadoMunicipio]

class MunicipioDescoberto(BaseModel):
    municipio: str
    uf: str
    codigo_ibge: str = ""
    site_prefeitura: str = ""
    status: str
    candidatos_testados: List[str] = []

class MunicipiosDiscoveryResponse(BaseModel):
    uf: str
    total_municipios: int
    encontrados: int
    nao_encontrados: int
    resultados: List[MunicipioDescoberto]
