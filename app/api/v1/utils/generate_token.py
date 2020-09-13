import requests
from requests.auth import HTTPBasicAuth
from ..utils import keys

def generate_token():
    response = requests.get(keys.mpesa_auth_url, auth = HTTPBasicAuth(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)).json()
    access_token = response['access_token']

    return access_token
