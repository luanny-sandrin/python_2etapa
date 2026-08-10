from flask_sqlalchemy import SQLAlchemy

# Um único objeto db para a aplicação; os Models escolhem o arquivo SQLite com __bind_key__.
db = SQLAlchemy()

from .base import ModeloBase
from .coleta_ge import ColetaGe
from .mencao_ge import MencaoGe

__all__ = ["db", "ModeloBase", "ColetaGe", "MencaoGe"]
