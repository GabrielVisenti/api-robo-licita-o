from fastapi import APIRouter

from app.models.schemas import BuscarLicitacoesRequest, BuscarLicitacoesResponse
from app.services.search_service import executar_busca_licitacoes

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "online",
        "message": "API GV CONNECT funcionando",
        "service": "gvconnect-crawler-api"
    }

@router.post("/buscar-licitacoes", response_model=BuscarLicitacoesResponse)
def buscar_licitacoes(payload: BuscarLicitacoesRequest):
    return executar_busca_licitacoes(payload)
