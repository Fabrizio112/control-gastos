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
    categoria=request.json["id_categoria"]
    nuevo_ingreso=IngresoModel(nro=0,monto=monto,descripcion=descripcion,fecha=datetime.now(),id_registro=id_registro,id_categoria=categoria)
    db.session.add(nuevo_ingreso)
    db.session.commit()
    return {'message':'Ingreso Añadido Correctamente'}

@ingreso_router.route("/ingreso/<id_registro>",methods=["GET"])
def get_all_ingresos_from_a_usuario(id_registro):
    ingresos=IngresoModel.query.filter_by(id_registro=id_registro).order_by(IngresoModel.fecha.desc()).all()
    results=ingresos_schema.dump(ingresos)
    return jsonify(results)


@ingreso_router.route("/ingreso/<nro>",methods=["GET"])
def get_ingreso(nro):
    ingreso=IngresoModel.query.get(nro)
    return ingreso_schema.jsonify(ingreso)

@ingreso_router.route("/ingreso/<nro>",methods=["PUT"])
def update_ingreso(nro):
    ingreso=IngresoModel.query.get(nro)
    ingreso.monto=request.json["monto"]
    ingreso.descripcion=request.json["descripcion"]
    ingreso.fecha=datetime.now()
    db.session.commit()
    return ingreso_schema.jsonify(ingreso)

@ingreso_router.route("/ingreso/<nro>",methods=["DELETE"])
def delete_ingreso(nro):
    ingreso=IngresoModel.query.get(nro)
    db.session.delete(ingreso)
    db.session.commit()
    return ingreso_schema.jsonify(ingreso)
