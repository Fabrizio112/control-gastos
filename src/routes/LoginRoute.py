from flask import Blueprint,request,jsonify
from ..models.UsuarioModel import UsuarioModel,usuario_schema
from werkzeug.security import generate_password_hash,check_password_hash
from ..utils import db,ma

login_router=Blueprint("login_rotuer",__name__)

@login_router.route("/login",methods=["POST"])
def login():
    email=request.json["email"]
    password=request.json["password"]
    usuario_a_logear=UsuarioModel.query.get(email)
    if usuario_a_logear != None:
        usuario_dict=usuario_schema.dump(usuario_a_logear)
        password_check=check_password_hash(usuario_dict["password"],password)
        if password_check == True:
            return {"message":"Acceso con exito","success":True},200
        else:
            return {"error":"Credenciales Invalidas"},404
    else:
        return {"error":"Credenciales Invalidas",'success':False},404

@login_router.route("/signup",methods=["POST"])
def signup():
    email=request.json["email"]
    nombre=request.json["nombre"]
    apellido=request.json["apellido"]
    username=request.json["username"]
    avatar=request.json["avatar"] or None
    password=request.json["password"]

    usuario_existe=UsuarioModel.query.get(email)
    if usuario_existe is None:
        username_existe=UsuarioModel.query.get(username)
        if username_existe is None:
            usuario_a_registrar=UsuarioModel(email=email,nombre=nombre,apellido=apellido,username=username,avatar=avatar,password=generate_password_hash(password))
            db.session.add(usuario_a_registrar)
            db.session.commit()
            return {'message':"Usuario Creado con Exito"},200
        else:
            return {"error":"Nombre de Usuario  ya en Uso"},404
    else:
        return {"error":"Usuario ya en Uso"},404
