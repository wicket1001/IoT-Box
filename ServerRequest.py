import requests
from requests.auth import HTTPBasicAuth
from credential import *


def modifyCustomerProfile():
    suffix = "/1/customers/" + cid
    data = {
      "street": "enter street",
      "city": "enter city",
      "note": "enter note"
    }
    return requests.put(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))



