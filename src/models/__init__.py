from ..utils import db,ma

categoria_x_egreso=db.Table("categoria_x_egreso",
db.Column("id",db.Integer,primary_key=True),
db.Column("nro_egreso",db.Integer,db.ForeignKey("egreso.nro")),
db.Column("id_categoria",db.Integer,db.ForeignKey("categoria.id"))
)                                                

categoria_x_ingreso=db.Table("categoria_x_ingreso",
db.Column("id",db.Integer,primary_key=True),
db.Column("nro_ingreso",db.Integer,db.ForeignKey("ingreso.nro")),
db.Column("id_categoria",db.Integer,db.ForeignKey("categoria.id"))
) 







