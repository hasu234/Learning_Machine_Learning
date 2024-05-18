import requests
import json
from requests.auth import HTTPBasicAuth


headers = {
    'Content-type':'application/json', 
    'Accept':'application/json'
}
url = ''
data = {"username":"admin","password":"admin"}

r = requests.post(
    url, 
    # auth=HTTPBasicAuth('admin', 'admin'), 
    json=data, 
    headers=headers
)
print(r.status_code)
