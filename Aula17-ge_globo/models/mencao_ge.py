# Cada linha = uma menção a "seleção" gravada naquela coleta (snapshot da API).

from . import db
from .base import ModeloBase


class MencaoGe(ModeloBase):
    __bind_key__ = "historico"
    __tablename__ = "mencoes_ge"

    coleta_id = db.Column(
        db.Integer,
        db.ForeignKey("coletas_ge.id"),
        nullable=False,
    )
    texto = db.Column(db.Text, nullable=False)
    trecho = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(500))
    tag = db.Column(db.String(20), nullable=False)

    coleta = db.relationship("ColetaGe", back_populates="mencoes")

    def para_dict(self) -> dict:
        return {
            "id": self.id,
            "coleta_id": self.coleta_id,
            "texto": self.texto,
            "trecho": self.trecho,
            "url": self.url,
            "tag": self.tag,
            "data_criacao": str(self.data_criacao),
            "data_atualizacao": str(self.data_atualizacao),
        }
