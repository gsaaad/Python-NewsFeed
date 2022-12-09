from flask import Flask
from app.routes import home, dashboard
from app.db import init_db
# activate venv
# .\venv\Scripts\activate

def create_app(test_config=None):
    # set up app oncfig
    
    
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(SECRET_KEY = 'super_secret_key')
    
    # add routes
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    
    #register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    
    # when flask is ready:
    init_db()
    return app