from flask import Blueprint,request,jsonify
from ..models.IngresoModel import IngresoModel,ingresos_schema
from ..models.categoria_x_ingreso import categoria_x_ingreso
from ..utils import db

CxI_router=Blueprint("CxI_router",__name__)

@CxI_router.route("/categoria-ingreso",methods=["POST"])
def add_cxi():
    nro_ingreso=request.json["nro_ingreso"]
    id_categoria=request.json["id_categoria"]
    cxi=categoria_x_ingreso(id=0,nro_ingreso=nro_ingreso,id_categoria=id_categoria)
    db.session.add(cxi)
    db.session.commit()
    return jsonify(cxi)

@CxI_router.route("/categoria-ingreso",methods=["GET"])
def get_cxi_categoria():
    id_registro=request.json["id_registro"]
    ingresos_con_id_registro=IngresoModel.query.filter_by(id_registro=id_registro).all()
    ingresos_dict=ingresos_schema.dump(ingresos_con_id_registro)
    results=[]
    for ingreso in ingresos_dict:
        cxi=categoria_x_ingreso.query.get(nro_ingreso=ingreso["nro"])
        results.append(cxi)
    return jsonify(results)
    
@CxI_router.route("/categoria-ingreso/<id>",methods=["DELETE"])
def delete_cxi(id):
    cxi_a_eliminar=categoria_x_ingreso.query.get(id)
    db.session.delete(cxi_a_eliminar)
    db.session.commit()
    return jsonify(cxi_a_eliminar)

