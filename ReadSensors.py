import requests
import json
from requests.auth import HTTPBasicAuth
from credential import *

data = {
    "select": [
        "ch0",
        "ch3",
        "ch1"
    ]
}

url = "https://3iot.drei.at/api"
suffix = "/1/customers/"+ cid + "/sites/" + sid + "/histdata0/youngest"

suffix = "/1/customers/" + cid + "/sites"

r = requests.get(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))
print(r.status_code)

print(str(r.json()))

parsed = json.loads(str(r.json()))

print(json.dumps(parsed, indent=4, short_keys=False))


