import os
#from werkzeug.contrib.fixers import ProxyFix
from app import create_app

APP = create_app(os.getenv("FLASK_ENV"))
#APP.wsgi_app = ProxyFix(APP.wsgi.app)

if __name__ == "__main__":
    APP.run()

