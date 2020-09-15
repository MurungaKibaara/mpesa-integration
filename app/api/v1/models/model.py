'''Define Transactions Functions'''
import requests
import base64
from ..utils.generate_token import generate_token
from ..utils.generate_timestamp import generate_timestamp
from ..utils.generate_password import generate_password
from ..utils import keys

def register_urls():
    '''Register Validation and confirmation urls'''
    access_token = generate_token()

    headers = {"Authorization": "Bearer %s" % access_token}

    request_body = {
        "ShortCode": keys.c2b_short_code,
        "ResponseType": "Completed",
        "ConfirmationURL": keys.BASE_URL + "/c2b/confirm",
        "ValidationURL": keys.BASE_URL + "/c2b/validation"
    }

    response = requests.post(keys.mpesa_endpoint, json=request_body, headers=headers)

    return response.json()

def simulate_transaction():
    '''Simulate a c2b transaction'''
    access_token = generate_token()
    headers = {"Authorization": "Bearer %s" % access_token}

    request_body = {
        "ShortCode": keys.c2b_short_code,
        "CommandID" : "CustomerPayBillOnline",
        "BillRefNumber": "Testpay1",
        "Msisdn": "254708374149",
        "Amount": 1
    }

    response = requests.post(keys.mpesa_simulation_endpoint, json=request_body, headers=headers)

    return response.json()

def simulate_lnm_request():
    '''Simulate LNM Request'''
    
    access_token = generate_token()
    password = generate_password()
    timestamp = generate_timestamp()

    headers = {"Authorization": "Bearer %s" % access_token}

    request_body = {
      "BusinessShortCode": keys.lnm_short_code,
      "Password": password,
      "Timestamp": timestamp,
      "TransactionType": "CustomerPayBillOnline",
      "Amount": 1,
      "PartyA": "254719562555",
      "PartyB": keys.lnm_short_code,
      "PhoneNumber": "254719562555",
      "CallBackURL": keys.BASE_URL + "/c2b/confirm",
      "AccountReference": "Test",
      "TransactionDesc": "Test"
    }

    response = requests.post(keys.mpesa_lnm_endpoint, json=request_body, headers=headers)

    return response.json()

