from dataclasses import dataclass


@dataclass
class DiscoveryResult:
    site_oficial: str | None = None
    diario_oficial: str | None = None
    portal_licitacoes: str | None = None
    portal_transparencia: str | None = None

    status: str = "PENDENTE"

    provider: str | None = None

    observacao: str | None = None