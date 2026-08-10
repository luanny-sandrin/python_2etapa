# Uma "foto" de cada vez que a API do GE foi consultada e salva no histórico.
# Vive no segundo banco SQLite (bind historico) — ver app.py.

from . import db
from .base import ModeloBase


class ColetaGe(ModeloBase):
    __bind_key__ = "historico"
    __tablename__ = "coletas_ge"

    fonte = db.Column(db.String(255), nullable=False)
    termo_busca = db.Column(db.String(80), nullable=False)
    modo_busca = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Integer, nullable=False, default=0)

    # relationship: uma coleta → várias menções (Aula 11, FK na filha).
    mencoes = db.relationship(
        "MencaoGe",
        back_populates="coleta",
        cascade="all, delete-orphan",
    )

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()

    def para_dict(self, incluir_mencoes: bool = False) -> dict:
        dados = {
            "id": self.id,
            "fonte": self.fonte,
            "termo_busca": self.termo_busca,
            "modo_busca": self.modo_busca,
            "total": self.total,
            "data_criacao": str(self.data_criacao),
            "data_atualizacao": str(self.data_atualizacao),
        }
        if incluir_mencoes:
            dados["mencoes"] = [m.para_dict() for m in self.mencoes]
        return dados
