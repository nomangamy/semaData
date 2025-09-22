from flask import Flask 
from Config import config 
from models import db 



def create_SemaData_app(config_class=config.Config):
    app =Flask(__name__)

    db.init_app(app)

    return app

if __name__ =='__main__':
    app = create_SemaData_app()
    app.run(debug=True)
