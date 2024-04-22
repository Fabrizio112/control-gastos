from ..utils import db,ma
from .categoria_x_egreso import categoria_x_egreso
from .categoria_x_ingreso import categoria_x_ingreso

class CategoriaModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    egresos=db.relationship("EgresoModel",secondary=categoria_x_egreso,backref="categoria_egresos")
    ingresos=db.relationship("IngresoModel",secondary=categoria_x_ingreso,backref="categoria_ingresos")

class CategoriaSchema(ma.Schema):
    class Meta:
        fields=('id','nombre')

categoria_schema=CategoriaSchema()
categorias_schema=CategoriaSchema(many=True)
