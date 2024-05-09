from flask import Blueprint,request,jsonify
from ..models.CategoriaModel import CategoriaModel,categoria_schema,categorias_schema
from ..utils import db
from ..utils.categories_default import categorias

categoria_router=Blueprint("categoria_router",__name__)


@categoria_router.route("/insertar-categorias")
def insertar_categorias():
    for nombre_categoria in categorias:
        categoria=CategoriaModel(id=0,nombre=nombre_categoria)
        db.session.add(categoria)
    db.session.commit()
    return "Categorias insertadas correctamente"


@categoria_router.route("/category",methods=["POST"])
def add_categoria():
    nombre=request.json["nombre"]
    categoria_a_añadir=CategoriaModel(id=0,nombre=nombre)
    db.session.add(categoria_a_añadir)
    db.session.commit()
    return categoria_schema.jsonify(categoria_a_añadir)

@categoria_router.route("/category",methods=["GET"])
def get_all_categories():
    categorias=CategoriaModel.query.order_by(CategoriaModel.id).all()
    results=categorias_schema.dump(categorias)
    return jsonify(results)

@categoria_router.route("/category/<id>",methods=["GET"])
def get_category(id):
    categoria=CategoriaModel.query.get(id)
    return categoria_schema.jsonify(categoria)

@categoria_router.route("/category/<id>",methods=["PUT"])
def edit_category(id):
    categoria=CategoriaModel.query.get(id)
    categoria.nombre=request.json["categoria"]
    db.session.commit()
    return categoria_schema.jsonify(categoria)
@categoria_router.route("/category/<id>",methods=["DELETE"])
def delete_category(id):
    categoria=CategoriaModel.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)