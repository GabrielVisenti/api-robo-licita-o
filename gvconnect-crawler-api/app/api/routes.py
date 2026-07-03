from fastapi import APIRouter

from app.models.schemas import BuscarLicitacoesRequest, BuscarLicitacoesResponse, MunicipiosDiscoveryResponse
from app.services.search_service import executar_busca_licitacoes, executar_discovery_municipios

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "online",
        "message": "API GV CONNECT funcionando",
        "service": "gvconnect-crawler-api",
        "sprint": "2 - Descoberta de municípios e sites oficiais",
    }

@router.get("/municipios/{uf}", response_model=MunicipiosDiscoveryResponse)
def descobrir_municipios(uf: str):
    return executar_discovery_municipios(uf)

@router.post("/buscar-licitacoes", response_model=BuscarLicitacoesResponse)
def buscar_licitacoes(payload: BuscarLicitacoesRequest):
    return executar_busca_licitacoes(payload)
