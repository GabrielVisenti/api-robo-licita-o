# GV Radar Brasil - Arquitetura do Sistema

## Visão Geral

O GV Radar é uma plataforma nacional de monitoramento de licitações públicas.

Seu objetivo é localizar automaticamente novas oportunidades de licitação em todos os municípios brasileiros, analisar seu conteúdo utilizando Inteligência Artificial e disponibilizar somente as oportunidades relevantes para a GV CONNECT.

---

# Fluxo Geral

Municípios
↓

Prefeituras
↓

Sites Oficiais
↓

Diários Oficiais
↓

Publicações

↓

OCR (quando necessário)

↓

Extração de Texto

↓

IA

↓

Licitações

↓

Dashboard

↓

Alertas

---

# Módulos

## 1. Cadastro Nacional de Municípios

Responsável por manter os 5.571 municípios atualizados.

Status:
✅ Concluído

---

## 2. Cadastro Nacional de Prefeituras

Responsável por armazenar:

- Site oficial
- Diário Oficial
- Portal de Licitações
- Portal da Transparência
- Status
- Observações
- Última verificação

Status:
🚧 Em desenvolvimento

---

## 3. Descoberta Inteligente de Prefeituras

Objetivo:

Descobrir automaticamente o site oficial de cada prefeitura.

Após encontrado:

Salvar permanentemente no banco.

---

## 4. Descoberta do Diário Oficial

Encontrar automaticamente onde cada município publica seu Diário Oficial.

---

## 5. Crawler

Responsável por baixar diariamente:

- PDFs
- HTML
- DOC
- DOCX

---

## 6. OCR

Quando o diário for imagem.

---

## 7. Extração de Texto

Normalização do conteúdo.

---

## 8. Inteligência Artificial

Responsável por identificar:

- Licitações
- Dispensas
- Credenciamentos
- Concorrências
- Pregões
- Chamamentos Públicos

Também será responsável por:

- Classificação
- Resumo
- Palavras-chave
- Priorização

---

## 9. Dashboard

Painel principal do sistema.

---

## 10. Alertas

Envio automático para:

- Sistema
- Email
- WhatsApp (futuro)

---

# Banco de Dados

Tabelas atuais:

- municipios
- prefeituras

Tabelas futuras:

- diarios
- publicacoes
- licitacoes
- anexos
- palavras_chave
- execucoes
- logs

---

# Objetivo Final

Monitorar automaticamente todo o território nacional e identificar oportunidades de licitação para a GV CONNECT de forma rápida, inteligente e escalável.