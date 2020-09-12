from flask import Blueprint, request, jsonify

MPESA = Blueprint('retrieve', __name__)

@MPESA.route('/retrieve', methods=['GET'])
def get():
    return jsonify({ "data": "transactions"})

@MPESA.route('/retrieve', methods=['POST'])
def post():
    return jsonify({ "data": "posted transactions"})