from ..utils import db

categoria_x_egreso=db.Table("categoria_x_egreso",
db.Column("id",db.Integer,primary_key=True),
db.Column("nro_egreso",db.Integer,db.ForeignKey("egreso_model.nro")),
db.Column("id_categoria",db.Integer,db.ForeignKey("categoria_model.id"))
)                                                
