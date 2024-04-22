from flask import Flask
from .utils import db,ma
from .routes.CategoriaRoutes import categoria_router
from .routes.CxE_Route import CxE_router
from .routes.CxI_Route import CxI_router
from .routes.EgresoRoute import egreso_router
from .routes.IngresoRoute import ingreso_router
from .routes.LoginRoute import login_router
from .routes.RegistroRoute import registros_router
from .routes.UserRoute import user_router
from flask_cors import CORS

def control_gastos_app():
    app=Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1234@localhost/control_gastos"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(categoria_router)
    app.register_blueprint(CxE_router)
    app.register_blueprint(CxI_router)
    app.register_blueprint(egreso_router)
    app.register_blueprint(ingreso_router)
    app.register_blueprint(login_router)
    app.register_blueprint(registros_router)
    app.register_blueprint(user_router)

    with app.app_context():
       db.create_all()
    
    return app


    """
        ACLARACION 1:
        Habia probado esta forma de crear las tablas y me resulto pero con la ayuda de la aclaracion 2 . Luego 
        hice un drop de la base de datos y probe creandola normal y funciono , asi que la conclusion fue 
        que el error no era por el orden de creacion de las tablas sino que era por el nombre de las tablas que
        MySQL le daba al momento de crearlas
        
        ACLARACION 2:
        Aclaracion importante MySQL le cambia el nombre a las tablas si se llamaban por ejemplo:
        UsuarioModelo , ahora vas a tener que poner de referencia de esa tabla como usuario_modelo , esto
        para las FOREIGNS KEYS
        
        from .models.UsuarioModel import UsuarioModel
        from .models.EgresoModel import EgresoModel
        from .models.IngresoModel import IngresoModel
        from .models.CategoriaModel import CategoriaModel
        from .models.RegistroModel import RegistroModel
        from .models.categoria_x_egreso import categoria_x_egreso
        from .models.categoria_x_ingreso import categoria_x_ingreso

        UsuarioModel.__table__.create(bind=db.engine)
        RegistroModel.__table__.create(bind=db.engine)
        EgresoModel.__table__.create(bind=db.engine)
        IngresoModel.__table__.create(bind=db.engine)
        CategoriaModel.__table__.create(bind=db.engine)
        categoria_x_egreso.create(bind=db.engine)
        categoria_x_ingreso.create(bind=db.engine)
        
        
        """

 