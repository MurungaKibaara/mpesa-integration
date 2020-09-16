
'''Application Entry Point'''
import os
import logging
from app import create_app

APP = create_app(os.getenv("FLASK_ENV"))

if __name__ == "__main__":
    APP.run()