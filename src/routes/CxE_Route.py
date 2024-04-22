from flask import Blueprint,request,jsonify
from ..models.EgresoModel import EgresoModel,egresos_schema
from ..models.categoria_x_egreso import categoria_x_egreso
from ..utils import db

CxE_router=Blueprint("CxE_router",__name__)

@CxE_router.route("/categoria-egreso",methods=["POST"])
def add_cxe():
    nro_egreso=request.json["nro_egreso"]
    id_categoria=request.json["id_categoria"]
    cxe=categoria_x_egreso(id=0,nro_egreso=nro_egreso,id_categoria=id_categoria)
    db.session.add(cxe)
    db.session.commit()
    return jsonify(cxe)

@CxE_router.route("/categoria-egreso",methods=["GET"])
def get_cxe_categoria():
    id_registro=request.json["id_registro"]
    egresos_con_id_registro=EgresoModel.query.filter_by(id_registro=id_registro).all()
    egresos_dict=egresos_schema.dump(egresos_con_id_registro)
    results=[]
    for egreso in egresos_dict:
        cxe=categoria_x_egreso.query.get(nro_egreso=egreso["nro"])
        results.append(cxe)
    return jsonify(results)
    
@CxE_router.route("/categoria-egreso/<id>",methods=["DELETE"])
def delete_cxe(id):
    cxe_a_eliminar=categoria_x_egreso.query.get(id)
    db.session.delete(cxe_a_eliminar)
    db.session.commit()
    return jsonify(cxe_a_eliminar)
