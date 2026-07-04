from app.constants.status import PrefeituraStatus
from app.models.prefeitura import Prefeitura


class PrefeituraService:

    def __init__(self, prefeitura_repository):
        self.prefeitura_repository = prefeitura_repository

    def buscar_por_municipio_id(self, municipio_id: int):
        return self.prefeitura_repository.buscar_por_municipio_id(municipio_id)

    def criar_prefeitura(self, municipio_id: int):
        prefeitura = Prefeitura(
            municipio_id=municipio_id,
            status=PrefeituraStatus.PENDENTE,
        )

        self.prefeitura_repository.criar(prefeitura)
        self.prefeitura_repository.salvar_alteracoes()

        return prefeitura