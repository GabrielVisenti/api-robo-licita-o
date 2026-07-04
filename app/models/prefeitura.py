from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Prefeitura(Base):
    __tablename__ = "prefeituras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    municipio_id: Mapped[int] = mapped_column(
        ForeignKey("municipios.id"),
        nullable=False,
        unique=True,
    )

    site_oficial: Mapped[str | None] = mapped_column(String(255), nullable=True)

    diario_oficial: Mapped[str | None] = mapped_column(String(255), nullable=True)

    portal_licitacao: Mapped[str | None] = mapped_column(String(255), nullable=True)

    status: Mapped[str] = mapped_column(String(50), default="PENDENTE")

    observacao: Mapped[str | None] = mapped_column(String(500), nullable=True)

    ultima_verificacao: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    municipio = relationship("Municipio", back_populates="prefeitura")