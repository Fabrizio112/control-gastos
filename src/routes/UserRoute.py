from flask import Blueprint,request
from..models.UsuarioModel import UsuarioModel,usuario_schema
from ..models.RegistroModel import RegistroModel
from ..utils.extensions import db
from werkzeug.security import generate_password_hash

user_router=Blueprint("user_rotuer",__name__)

@user_router.route("/user/<email>",methods=["GET"])
def get_user_by_email(email):
    usuario_en_particular=UsuarioModel.query.get(email)
    return usuario_schema.jsonify(usuario_en_particular)

@user_router.route("/user/<email>",methods=["PUT"])
def update_user(email):
    if request.json["password"] == None:
        usuario_a_actualizar=UsuarioModel.query.get(email)
        usuario_a_actualizar.nombre=request.json["nombre"]
        usuario_a_actualizar.apellido=request.json["apellido"]
        usuario_a_actualizar.username=request.json["username"]
        usuario_a_actualizar.avatar=request.json["username"] or None
        db.session.commit()
        return usuario_schema.jsonify(usuario_a_actualizar)
    else:
        usuario_a_actualizar=UsuarioModel.query.get(email)
        usuario_a_actualizar.password=generate_password_hash(request.json["password"])
        db.session.commit()
        return usuario_schema.jsonify(usuario_a_actualizar)

@user_router.route("/user/<email>",methods=["DELETE"])
def delete_user(email):
    registros_del_usuario=RegistroModel.query.filter_by(email_usuario=email).all()
    from .RegistroRoute import delete_registro
    for registro in registros_del_usuario:
        delete_registro(registro.id)
    usuario_a_eliminar=UsuarioModel.query.get(email)
    db.session.delete(usuario_a_eliminar)
    db.session.commit()
    return usuario_schema.jsonify(usuario_a_eliminar),200
