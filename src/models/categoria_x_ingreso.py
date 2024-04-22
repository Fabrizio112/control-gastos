from ..utils import db
 
categoria_x_ingreso=db.Table("categoria_x_ingreso",
db.Column("id",db.Integer,primary_key=True),
db.Column("nro_ingreso",db.Integer,db.ForeignKey("ingreso_model.nro")),
db.Column("id_categoria",db.Integer,db.ForeignKey("categoria_model.id"))
)
