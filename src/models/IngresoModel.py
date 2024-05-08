from ..utils import db,ma
from datetime import datetime

class IngresoModel(db.Model):
    nro=db.Column(db.Integer,primary_key=True)
    monto=db.Column(db.Integer,nullable=False)
    descripcion=db.Column(db.Text,nullable=True)
    fecha=db.Column(db.DateTime,default=datetime.now())
    id_registro=db.Column(db.Integer,db.ForeignKey("registro_model.id"))
    id_categoria=db.Column(db.Integer,db.ForeignKey("categoria_model.id"))

class IngresoSchema(ma.Schema):
    class Meta:
        fields=('nro','monto','descripcion','fecha','id_registro','id_categoria')

ingreso_schema=IngresoSchema()
ingresos_schema=IngresoSchema(many=True)