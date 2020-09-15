from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CONSUMER_KEY = getenv("CONSUMER_KEY")
CONSUMER_SECRET = getenv("CONSUMER_SECRET")
mpesa_auth_url = getenv("mpesa_auth_url")
BASE_URL= getenv("BASE_URL")
c2b_short_code = getenv("c2b_short_code")
mpesa_endpoint = getenv("mpesa_endpoint")
mpesa_simulation_endpoint = getenv("mpesa_simulation_endpoint")
lnm_short_code = getenv("lnm_short_code")
lnm_pass_key = getenv("lnm_pass_key")
mpesa_lnm_endpoint = getenv("mpesa_lnm_endpoint")
