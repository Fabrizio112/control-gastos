from ..utils import db,ma

class UsuarioModel(db.Model):
    email=db.Column(db.String(100),primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    apellido=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(100),unique=True)
    avatar=db.Column(db.String(255),nullable=True)
    password=db.Column(db.String(255),nullable=False)
    registro=db.relationship("RegistroModel",backref="usuario")

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('email','nombre','apellido','username','avatar','password')

usuario_schema=UsuarioSchema()
usuarios_schema=UsuarioSchema(many=True)
