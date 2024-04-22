from flask import Blueprint,request,jsonify
from ..models.IngresoModel import IngresoModel,ingreso_schema,ingresos_schema
from ..utils import db
from datetime import datetime
ingreso_router=Blueprint("ingreso_router",__name__)



@ingreso_router.route("/ingreso",methods=["POST"])
def add_ingreso():
    id_registro=request.json["id_registro"]
    monto=request.json["monto"]
    descripcion=request.json["descripcion"] or None
    nuevo_ingreso=IngresoModel(id=0,monto=monto,descripcion=descripcion,id_registro=id_registro)
    db.session.add(nuevo_ingreso)
    db.session.commit()
    return ingreso_schema.jsonify(nuevo_ingreso)

@ingreso_router.route("/ingreso",methods=["GET"])
def get_all_ingresos_from_a_usuario():
    id_registro=request.json["id_registro"]
    ingresos=IngresoModel.query.filter_by(id_registro=id_registro).all()
    results=ingresos_schema.dump(ingresos)
    return jsonify(results)

@ingreso_router.route("/ingreso/<id>",methods=["GET"])
def get_ingreso(id):
    ingreso=IngresoModel.query.get(id)
    return ingreso_schema.jsonify(ingreso)

@ingreso_router.route("/ingreso/<id>",methods=["PUT"])
def update_ingreso(id):
    ingreso=IngresoModel.query.get(id)
    ingreso.monto=request.json["monto"]
    ingreso.descripcion=request.json["descripcion"]
    ingreso.fecha=datetime.now()
    db.session.commit()
    return ingreso_schema.jsonify(ingreso)

@ingreso_router.route("/ingreso/<id>",methods=["DELETE"])
def delete_ingreso(id):
    ingreso=IngresoModel.query.get(id)
    db.session.delete(ingreso)
    db.session.commit()
    return ingreso_schema.jsonify(ingreso)
