from flask import Flask
from app.routes import home, dashboard, api

# db
from app.db import init_db

#filters

from app.utils import filters

# activate venv
# .\venv\Scripts\activate



def create_app(test_config=None):
    # set up app config
    
    
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    # secret key
    app.config.from_mapping(SECRET_KEY = 'super_secret_key')
    
    # filter functions
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters["format_date"] = filters.format_date
    app.jinja_env.filters["format_plural"] = filters.format_plural
    print("FILTERS",app.jinja_env.filters)
    
    # add routes
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    
    #register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    
    # db connection
    init_db(app)
    return app