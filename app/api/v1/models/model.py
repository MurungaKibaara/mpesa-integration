'''Define Transactions Functions'''
import requests
from ..utils.generate_token import generate_token
from ..utils import keys

def register_urls():
    '''Register Validation and confirmation urls'''
    access_token = generate_token()

    headers = {"Authorization": "Bearer %s" % access_token}

    request_body = {
        "shortCode": keys.shortCode,
        "ResponseType": "Completed",
        "ConfirmationURL": keys.BASE_URL + "/c2b/confirmation",
        "ValidationURL": keys.BASE_URL + "/c2b/validation"
    }

    response = requests.post(keys.mpesa_endpoint, json=request_body, headers=headers)

    return response.json()