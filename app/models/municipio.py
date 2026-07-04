from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Municipio(Base):
    __tablename__ = "municipios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    codigo_ibge: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)

    nome: Mapped[str] = mapped_column(String(150), nullable=False)

    uf: Mapped[str] = mapped_column(String(2), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )