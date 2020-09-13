import base64
from ..utils.generate_timestamp import generate_timestamp
from ..utils import keys

def generate_password():
    timestamp = generate_timestamp()
    
    password = keys.lnm_short_code + keys.lnm_pass_key + timestamp
    password = base64.b64encode(bytes(password, 'utf-8')).decode('utf-8')

    return password
