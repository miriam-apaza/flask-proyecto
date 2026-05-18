import logging
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)

# Configuración del entorno
app.config["SECRET_KEY"] = "clave_secreta_instituto_2026"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instituto.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

# Importación de las nuevas vistas académicas
from . import views
