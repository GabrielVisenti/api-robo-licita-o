from sqlalchemy.orm import Session

from app.models.prefeitura import Prefeitura


class PrefeituraRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_por_municipio_id(self, municipio_id: int):
        return (
            self.db.query(Prefeitura)
            .filter(Prefeitura.municipio_id == municipio_id)
            .first()
        )

    def criar(self, prefeitura: Prefeitura):
        self.db.add(prefeitura)
        return prefeitura

    def salvar_alteracoes(self):
        self.db.commit()