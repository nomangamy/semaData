import Flask
from Config import Config
from extensions import db 
from Config import Development 
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt


from Routes.Auth.register import register_bp




def semaData_app():
    app =Flask(__name__)
    db.init_app(app)
    bcrypt = Bcrypt(app)
    migrate = Migrate(app,db)
    CORS(app)
    app.config.from_object(Config)
    db.Config.from_object(Development)

    app.register_blueprint(register_bp,url_prefix='/api') 


    return app 