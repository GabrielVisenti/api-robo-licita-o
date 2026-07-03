# GV CONNECT Crawler API

API externa do **Radar de Licitações Municipais — GV CONNECT**.

Esta primeira versão foi criada para validar a integração com a Base44.
Ela já possui a estrutura profissional para evoluir para crawler real com leitura de Diários Oficiais, PDFs, OCR e classificação por IA.

## Endpoints

### Teste de saúde

```http
GET /api/health
```

### Buscar licitações

```http
POST /api/buscar-licitacoes
```

Payload:

```json
{
  "estado": "Paraná",
  "uf": "PR",
  "data_diario": "2026-07-03"
}
```

## Rodar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Abrir:

```text
http://127.0.0.1:8000/api/health
```

Documentação automática:

```text
http://127.0.0.1:8000/docs
```

## Deploy no Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Importante

No GitHub, os arquivos `main.py`, `requirements.txt`, `render.yaml` e a pasta `app` devem ficar na raiz do repositório.

Estrutura esperada:

```text
gvconnect-crawler-api/
├── app/
├── main.py
├── requirements.txt
├── render.yaml
├── README.md
└── .gitignore
```
