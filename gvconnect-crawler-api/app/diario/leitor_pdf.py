from pathlib import Path
import pdfplumber

def extrair_texto_pdf(caminho_pdf: str) -> str:
    caminho = Path(caminho_pdf)
    if not caminho.exists():
        return ""

    partes: list[str] = []
    with pdfplumber.open(str(caminho)) as pdf:
        for pagina in pdf.pages:
            partes.append(pagina.extract_text() or "")
    return "\n".join(partes).strip()
