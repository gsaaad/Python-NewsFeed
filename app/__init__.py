from flask import Flask
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
    return app