# Grava no banco o resultado de buscar_mencoes_selecao (cada sincronização = nova coleta).

from models import ColetaGe, MencaoGe, db
from services.ge_globo import ResultadoBusca


def persistir_coleta(dados: ResultadoBusca) -> ColetaGe:
    """
    Chamado após atualizar/consultar a API externa.
    Cria ColetaGe + MencaoGe no SQLite historico_ge.db.
    """
    coleta = ColetaGe(
        fonte=dados["fonte"],
        termo_busca=dados["termo_busca"],
        modo_busca=dados["modo_busca"],
        total=dados["total"],
    )

    for item in dados["mencoes"]:
        coleta.mencoes.append(
            MencaoGe(
                texto=item["texto"],
                trecho=item["trecho"],
                url=item["url"],
                tag=item["tag"],
            )
        )

    db.session.add(coleta)
    db.session.commit()
    return coleta
