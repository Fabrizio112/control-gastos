from flask import Flask
from .utils import db,ma

def control_gastos_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]=""
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)
    ma.init_app(app)

    return app