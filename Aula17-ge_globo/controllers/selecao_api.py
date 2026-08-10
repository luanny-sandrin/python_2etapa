# Rotas da API ao vivo (GE) + sincronização que grava no banco historico_ge.db

from __future__ import annotations

from typing import Any

from flask import Blueprint, jsonify, request

from services import buscar_mencoes_selecao, persistir_coleta

selecao_api_bp = Blueprint("selecao_api", __name__, url_prefix="/api")


def _validar_modo() -> str | tuple[Any, int]:
    modo: str = request.args.get("modo", "substring").strip().lower()
    if modo not in ("substring", "palavra"):
        return jsonify(
            {"erro": "Parâmetro modo deve ser 'substring' ou 'palavra'"}
        ), 400
    return modo


@selecao_api_bp.route("/selecao", methods=["GET"])
def listar_mencoes_selecao() -> Any:
    """Aula 16: só consulta o GE, não grava no banco."""
    modo = _validar_modo()
    if isinstance(modo, tuple):
        return modo

    try:
        dados = buscar_mencoes_selecao(modo=modo)
    except ConnectionError as erro:
        return jsonify({"erro": str(erro)}), 502

    return jsonify(dados)


@selecao_api_bp.route("/selecao/sincronizar", methods=["POST"])
def sincronizar_selecao() -> Any:
    """
    Consulta o GE e grava uma nova ColetaGe + MencaoGe no segundo banco (historico).
    Cada POST = nova "atualização" persistida (data_criacao / data_atualizacao no Model).
    """
    modo = _validar_modo()
    if isinstance(modo, tuple):
        return modo

    try:
        dados = buscar_mencoes_selecao(modo=modo)
    except ConnectionError as erro:
        return jsonify({"erro": str(erro)}), 502

    coleta = persistir_coleta(dados)

    return jsonify(
        {
            "mensagem": "Coleta gravada no historico_ge.db",
            "coleta_id": coleta.id,
            "dados_api": dados,
        }
    ), 201
