# Lê coletas já gravadas no banco historico (não chama o GE de novo).

from __future__ import annotations

from typing import Any

from flask import Blueprint, jsonify

from models import ColetaGe, db

historico_api_bp = Blueprint("historico_api", __name__, url_prefix="/api/historico")


@historico_api_bp.route("/coletas", methods=["GET"])
def listar_coletas() -> Any:
    coletas = ColetaGe.listar()
    return jsonify([c.para_dict() for c in coletas])


@historico_api_bp.route("/coletas/<int:coleta_id>", methods=["GET"])
def detalhe_coleta(coleta_id: int) -> Any:
    coleta = db.session.get(ColetaGe, coleta_id)
    if not coleta:
        return jsonify({"erro": "Coleta não encontrada"}), 404
    return jsonify(coleta.para_dict(incluir_mencoes=True))
