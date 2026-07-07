from sqlalchemy.orm import Session, joinedload

from app.constants.status import PrefeituraStatus
from app.models.prefeitura import Prefeitura


class PrefeituraRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_por_municipio_id(self, municipio_id: int) -> Prefeitura | None:
        return (
            self.db.query(Prefeitura)
            .options(joinedload(Prefeitura.municipio))
            .filter(Prefeitura.municipio_id == municipio_id)
            .first()
        )

    def listar(self, limite: int = 100) -> list[Prefeitura]:
        return (
            self.db.query(Prefeitura)
            .options(joinedload(Prefeitura.municipio))
            .limit(limite)
            .all()
        )

    def listar_pendentes(self, limite: int = 10) -> list[Prefeitura]:
        return (
            self.db.query(Prefeitura)
            .options(joinedload(Prefeitura.municipio))
            .filter(Prefeitura.status == PrefeituraStatus.PENDENTE)
            .limit(limite)
            .all()
        )

    def criar(self, prefeitura: Prefeitura) -> Prefeitura:
        self.db.add(prefeitura)
        return prefeitura

    def salvar_alteracoes(self):
        self.db.commit()