import requests
from requests.auth import HTTPBasicAuth
from credential import *

#The first thing upon user login
def queryLoggedInUserAndCustomerList():
    suffix = '/1/me' + cid
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))

#Manage acustomer
def queryTheUsersCustomerList():
    suffix = '/1/customers' + cid
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))



def modifyCustomerProfile():
    suffix = "/1/customers/" + cid
    data = {
      "street": "enter street",
      "city": "enter city",
      "note": "enter note"
    }
    return requests.put(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))



