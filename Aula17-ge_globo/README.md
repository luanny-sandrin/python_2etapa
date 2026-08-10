# Aula 17 — API GE + histórico em banco

Igual à [Aula 16](../Aula16-ge_globo), com **models** que gravam cada sincronização.

## Dois bancos SQLite

| Arquivo | Uso |
|---------|-----|
| `principal.db` | Bind padrão (reservado; sem tabelas nesta aula) |
| `historico_ge.db` | `ColetaGe` + `MencaoGe` (cada POST sincronizar) |

## Models

- `ModeloBase` — `id`, `data_criacao`, `data_atualizacao`
- `ColetaGe` — um registro por atualização da API (fonte, modo, total)
- `MencaoGe` — FK `coleta_id`, menções daquela coleta

## Rotas

| Método | Rota |
|--------|------|
| GET | `/api/selecao` |
| POST | `/api/selecao/sincronizar` |
| GET | `/api/historico/coletas` |
| GET | `/api/historico/coletas/<id>` |

## Rodar

```powershell
cd flask/Aula17-ge_globo
pip install -r requirements.txt
python app.py
```

```powershell
curl -X POST "http://127.0.0.1:5000/api/selecao/sincronizar?modo=substring"
curl http://127.0.0.1:5000/api/historico/coletas
```

Roteiro: `Aula17.txt`.
