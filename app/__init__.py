import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from instance.config import APP_CONFIG, DevelopmentConfig
import logging
from logging import Formatter, FileHandler
# from app.api.v1.models.database import init_db, create_tables
from app.api.v1.views.view import MPESA


LOGGER = logging.getLogger('whatever')
file_handler = FileHandler('test.log')
handler = logging.StreamHandler()
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
LOGGER.addHandler(file_handler)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)

def create_app(config_name):
    '''create app'''
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    # app.config.from_object(APP_CONFIG[config_name])

    # with app.app_context():
    #     init_db()
    #     create_tables()

    app.config.from_pyfile('config.py')
    app.register_blueprint(MPESA, url_prefix='/api/v1')
    LOGGER.info('info log')
    LOGGER.debug('debug log')

    @app.errorhandler(404)
    def resource_not_found(message):
        """resource not found handler"""

        return jsonify({
            "status": 404,
            "message": str(message)
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(message):
        """ method not allowed error handler"""

        return jsonify({
            "status": 405,
            "message": str(message)
        }), 405

    @app.errorhandler(500)
    def internal_server_error(message):
        """ Internal server error handler """
        return jsonify({
            "status": 500,
            "message": str(message)
        }), 500

    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)

    return app

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)