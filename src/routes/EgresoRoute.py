from flask import Blueprint,request,jsonify
from ..models.EgresoModel import EgresoModel,egreso_schema,egresos_schema
from ..utils import db
from datetime import datetime
egreso_router=Blueprint("egreso_router",__name__)



@egreso_router.route("/egreso",methods=["POST"])
def add_egreso():
    id_registro=request.json["id_registro"]
    monto=request.json["monto"]
    descripcion=request.json["descripcion"] or None
    nuevo_egreso=EgresoModel(id=0,monto=monto,descripcion=descripcion,id_registro=id_registro)
    db.session.add(nuevo_egreso)
    db.session.commit()
    return egreso_schema.jsonify(nuevo_egreso)

@egreso_router.route("/egreso",methods=["GET"])
def get_all_egresos_from_a_usuario():
    id_registro=request.json["id_registro"]
    egresos=EgresoModel.query.filter_by(id_registro=id_registro).all()
    results=egresos_schema.dump(egresos)
    return jsonify(results)

@egreso_router.route("/egreso/<id>",methods=["GET"])
def get_egreso(id):
    egreso=EgresoModel.query.get(id)
    return egreso_schema.jsonify(egreso)

@egreso_router.route("/egreso/<id>",methods=["PUT"])
def update_egreso(id):
    egreso=EgresoModel.query.get(id)
    egreso.monto=request.json["monto"]
    egreso.descripcion=request.json["descripcion"]
    egreso.fecha=datetime.now()
    db.session.commit()
    return egreso_schema.jsonify(egreso)

@egreso_router.route("/egreso/<id>",methods=["DELETE"])
def delete_egreso(id):
    egreso=EgresoModel.query.get(id)
    db.session.delete(egreso)
    db.session.commit()
    return egreso_schema.jsonify(egreso)
