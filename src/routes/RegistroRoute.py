from flask import Blueprint,request,jsonify
from ..models.RegistroModel import RegistroModel,registros_schema,registro_schema
from ..models.EgresoModel import EgresoModel
from ..models.IngresoModel import IngresoModel
from ..utils import db

registros_router=Blueprint("registros_router",__name__)

@registros_router.route("/registro",methods=["POST"])
def create_registro():
    email_usuario=request.json["email"]
    registro_a_crear=RegistroModel(id=0,email_usuario=email_usuario)
    db.session.add(registro_a_crear)
    db.session.commit()
    return registro_schema.jsonify(registro_a_crear)

@registros_router.route("/registro/<email>",methods=["GET"])
def get_registros(email):
    email=request.json["email"]
    registro=RegistroModel.query.filter_by(email_user=email).all()
    results=registros_schema.dump(registro)
    return jsonify(results)

@registros_router.route("/registro/<id>",methods=["DELETE"])
def delete_registro(id):
    egresos_asociados_registro=EgresoModel.query.filter_by(id_registro=id).all()
    ingresos_asociados_registro=IngresoModel.query.filter_by(id_registro=id).all()
    registro_a_eliminar=RegistroModel.query.get(id)
    db.session.delete(egresos_asociados_registro)
    db.session.delete(ingresos_asociados_registro)
    db.session.delete(registro_a_eliminar)
    db.session.commit()
    return registro_schema.jsonify(registro_a_eliminar)


