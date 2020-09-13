from flask import Blueprint, request, jsonify
import json
from ..models.model import register_urls, simulate_transaction
MPESA = Blueprint('retrieve', __name__)

@MPESA.route('/register_urls', methods=['POST'])
def register_url():
    response_data = register_urls()
    return response_data

@MPESA.route('/simulate', methods=['POST'])
def simulate():
    response_data = simulate_transaction()
    return response_data

@MPESA.route('/c2b/confirm', methods=['POST'])
def confirm():
    data = request.get_json()
    file = open('confirm.json', 'a')
    file.write(json.dumps(data))
    file.close()
    return {"ResultCode": 0, "ResultDescription": "Accepted","ThirdPartyTransID": "MarsianInThisBitch" }

@MPESA.route('/c2b/validation', methods=['POST'])
def validate():
    data = request.get_json()
    file = open('validate.json', 'a')
    file.write(json.dumps(data))
    file.close()
    return {"ResultCode": 0, "ResultDescription": "Accepted", "ThirdPartyTransID": "MarsianInThisBitch" }