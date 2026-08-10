================================================================================
AULA 17 — AULA 16 + MODELS E HISTÓRICO NO SQLITE
================================================================================

  Aula 16  →  GET /api/selecao  →  só JSON ao vivo
  Aula 17  →  POST /api/selecao/sincronizar  →  GE + grava historico_ge.db

  ModeloBase (abstract): id, data_criacao, data_atualizacao
  ColetaGe + MencaoGe no bind "historico" (segundo arquivo .db)

  GET /api/historico/coletas  →  lista coletas salvas

================================================================================
