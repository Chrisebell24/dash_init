import requests

def check_if_not_running(port):
    try:
        status_code = requests.get(f'http://0.0.0.0:{port}').status_code
    except:
        status_code = None
        
    
    return status_code is None
