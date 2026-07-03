# GV CONNECT Crawler API

API externa do Radar de Licitações Municipais — GV CONNECT.

## Status

- Sprint 1: infraestrutura FastAPI + Render + Base44 ✅
- Sprint 2: lista real de municípios por UF via IBGE + descoberta automática de sites oficiais de prefeituras ✅

## Endpoints

### Saúde

```http
GET /api/health
```

### Descobrir municípios e sites oficiais

```http
GET /api/municipios/PR
```

Retorna todos os municípios da UF informada e tenta localizar automaticamente o site oficial da prefeitura.

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

Na Sprint 2, este endpoint ainda não lê Diários Oficiais. Ele retorna o status real de descoberta do site oficial de cada prefeitura. A leitura do Diário Oficial será implementada na Sprint 3.

## Deploy Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Python

Use Python 3.11.11.
