import re
import unicodedata


def remover_acentos(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(ch for ch in texto if not unicodedata.combining(ch))


def slug_municipio(nome: str) -> str:
    """Transforma nome do município em slug para testar domínios.

    Ex: São Jorge do Ivaí -> sao-jorge-do-ivai
    """
    texto = remover_acentos(nome).lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    texto = re.sub(r"-+", "-", texto).strip("-")
    return texto


def dominio_municipio(nome: str) -> str:
    """Slug sem hífen, usado por muitos domínios municipais.

    Ex: São Jorge do Ivaí -> saojorgedoivai
    """
    return slug_municipio(nome).replace("-", "")
