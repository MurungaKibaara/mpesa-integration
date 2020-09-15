from datetime import datetime

def generate_timestamp():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return timestamp