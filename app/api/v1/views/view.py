from flask import Blueprint, request, jsonify
import json
from ..models.model import register_urls
MPESA = Blueprint('retrieve', __name__)

@MPESA.route('/register_urls', methods=['GET'])
def register_url():
    response_data = register_urls()
    return response_data

@MPESA.route('/c2b/confirmation', methods=['POST'])
def confirm():
    data = request.get_json()
    file = open('confirm.json', 'a')
    file.write(data)
    file.close()

@MPESA.route('/c2b/validation', methods=['POST'])
def validate():
    data = request.get_json()
    file = open('validate.json', 'a')
    file.write(data)
    file.close()