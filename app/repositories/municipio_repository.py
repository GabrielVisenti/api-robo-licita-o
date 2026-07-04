from sqlalchemy.orm import Session

from app.models.municipio import Municipio


class MunicipioRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_por_codigo_ibge(self, codigo_ibge: str):
        return (
            self.db.query(Municipio)
            .filter(Municipio.codigo_ibge == codigo_ibge)
            .first()
        )

    def existe_codigo_ibge(self, codigo_ibge: str) -> bool:
        return self.buscar_por_codigo_ibge(codigo_ibge) is not None

    def criar(self, municipio: Municipio):
        self.db.add(municipio)
        return municipio

    def salvar_alteracoes(self):
        self.db.commit()