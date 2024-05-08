from ..utils import db,ma


class CategoriaModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False,unique=True)
    ingreso=db.relationship("IngresoModel",backref="categoria")
    egreso=db.relationship("EgresoModel",backref="categoria")

class CategoriaSchema(ma.Schema):
    class Meta:
        fields=('id','nombre')

categoria_schema=CategoriaSchema()
categorias_schema=CategoriaSchema(many=True)
