
'''Application Entry Point'''
import os
import logging
from app import create_app

APP = create_app(os.getenv("FLASK_ENV"))

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    APP.logger.handlers = gunicorn_logger.handlers
    APP.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    APP.run()