from datetime import datetime

from app.constants.status import PrefeituraStatus
from app.domain.discovery_result import DiscoveryResult
from app.models.prefeitura import Prefeitura


class PrefeituraService:

    def __init__(self, prefeitura_repository):
        self.prefeitura_repository = prefeitura_repository

    def buscar_por_municipio_id(self, municipio_id: int) -> Prefeitura | None:
        return self.prefeitura_repository.buscar_por_municipio_id(municipio_id)

    def listar_pendentes(self, limite: int = 10) -> list[Prefeitura]:
        return self.prefeitura_repository.listar_pendentes(limite)

    def criar_prefeitura(self, municipio_id: int) -> Prefeitura:
        prefeitura = Prefeitura(
            municipio_id=municipio_id,
            status=PrefeituraStatus.PENDENTE,
        )

        self.prefeitura_repository.criar(prefeitura)
        self.prefeitura_repository.salvar_alteracoes()

        return prefeitura

    def atualizar_descoberta(
        self,
        prefeitura: Prefeitura,
        resultado: DiscoveryResult,
    ) -> Prefeitura:

        prefeitura.site_oficial = resultado.site_oficial
        prefeitura.diario_oficial = resultado.diario_oficial
        prefeitura.portal_licitacao = resultado.portal_licitacoes

        prefeitura.status = resultado.status
        prefeitura.observacao = resultado.observacao

        prefeitura.ultima_verificacao = datetime.utcnow()

        self.prefeitura_repository.salvar_alteracoes()

        return prefeitura