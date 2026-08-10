# Aula 17 — Aula 16 + camada models com dois arquivos SQLite.
#
# Banco 1 (principal.db): reservado / bind padrão do Flask-SQLAlchemy (vazio nesta aula).
# Banco 2 (historico_ge.db): ColetaGe + MencaoGe — histórico de cada sincronização da API.

import os

from flask import Flask, jsonify

from controllers import historico_api_bp, selecao_api_bp
from models import db

ENDPOINTS: list[dict[str, str]] = [
    {
        "metodo": "GET",
        "rota": "/api/selecao",
        "descricao": "Busca ao vivo no GE (não grava)",
        "query": "?modo=substring ou palavra",
    },
    {
        "metodo": "POST",
        "rota": "/api/selecao/sincronizar",
        "descricao": "Busca no GE e grava coleta no historico_ge.db",
        "query": "?modo=substring ou palavra",
    },
    {
        "metodo": "GET",
        "rota": "/api/historico/coletas",
        "descricao": "Lista coletas gravadas",
    },
    {
        "metodo": "GET",
        "rota": "/api/historico/coletas/<id>",
        "descricao": "Detalhe de uma coleta com menções",
    },
]


def criar_app() -> Flask:
    app = Flask(__name__)
    pasta = os.path.abspath(os.path.dirname(__file__))

    # Dois bancos SQLite na pasta do projeto (ver models: __bind_key__ = "historico").
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "principal.db"
    )
    app.config["SQLALCHEMY_BINDS"] = {
        "historico": "sqlite:///" + os.path.join(pasta, "historico_ge.db"),
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "aula17-ge-globo-dev"

    db.init_app(app)
    app.register_blueprint(selecao_api_bp)
    app.register_blueprint(historico_api_bp)

    with app.app_context():
        # Cria tabelas no bind historico (e no principal, se no futuro houver Models sem bind).
        db.create_all()

    @app.route("/")
    def index():
        return jsonify(
            {
                "aula": "17 — GE + histórico em SQLite",
                "bancos": {
                    "principal": "principal.db (bind padrão)",
                    "historico": "historico_ge.db (coletas da API)",
                },
                "endpoints": ENDPOINTS,
            }
        )

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
