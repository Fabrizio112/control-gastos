from ..utils import db,ma

class RegistroModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email_usuario=db.Column(db.String(100),db.ForeignKey("usuario_model.email"))
    ingreso=db.relationship("IngresoModel",backref="Registro")
    egreso=db.relationship("EgresoModel",backref="Registro")

class RegistroSchema(ma.Schema):
    class Meta:
        fields=('id','id_usuario')

registro_schema=RegistroSchema()
registros_schema=RegistroSchema(many=True)