PALAVRAS_ALTA = [
    "toner", "cartucho", "impressora", "notebook", "computador", "monitor",
    "informática", "informatica", "ti", "tecnologia", "scanner", "ssd", "memória", "memoria"
]

def classificar_relevancia(objeto: str) -> str:
    texto = objeto.lower()
    if any(p in texto for p in PALAVRAS_ALTA):
        return "Alta"
    return "Baixa"
