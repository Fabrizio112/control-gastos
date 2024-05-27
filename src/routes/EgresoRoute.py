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
    categoria=request.json["id_categoria"]
    nuevo_egreso=EgresoModel(nro=0,monto=monto,descripcion=descripcion,fecha=datetime.now(),id_registro=id_registro,id_categoria=categoria)
    db.session.add(nuevo_egreso)
    db.session.commit()
    return {'message':"Egreso Añadido Con Exito "}

@egreso_router.route("/egreso/<id_registro>",methods=["GET"])
def get_all_egresos_from_a_usuario(id_registro):
    egresos=EgresoModel.query.filter_by(id_registro=id_registro).order_by(EgresoModel.fecha.desc()).all()
    results=egresos_schema.dump(egresos)
    return jsonify(results)



@egreso_router.route("/egreso/<nro>",methods=["GET"])
def get_egreso(nro):
    egreso=EgresoModel.query.get(nro)
    return egreso_schema.jsonify(egreso)

@egreso_router.route("/egreso/<nro>",methods=["PUT"])
def update_egreso(nro):
    egreso=EgresoModel.query.get(nro)
    egreso.monto=request.json["monto"]
    egreso.descripcion=request.json["descripcion"]
    egreso.fecha=datetime.now()
    db.session.commit()
    return egreso_schema.jsonify(egreso)

@egreso_router.route("/egreso/<nro>",methods=["DELETE"])
def delete_egreso(nro):
    egreso=EgresoModel.query.get(nro)
    db.session.delete(egreso)
    db.session.commit()
    return egreso_schema.jsonify(egreso)
