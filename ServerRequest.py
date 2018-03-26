import requests
from requests.auth import HTTPBasicAuth
from credential import *

#The first thing upon user login
def queryLoggedInUserAndCustomerList():
    suffix = '/1/me'
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))

#Manage acustomer
def queryTheUsersCustomerList():
    suffix = '/1/customers'
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))

def addNewCustomer():
    suffix  = '/1/customers'
    post = {
  "name": "enter name",
  "street": "enter street",
  "city": "enter city",
  "note": "enter note"
}
    return requests.post(url + suffix, json=post, auth=HTTPBasicAuth(cid, passwd))

def queryCustomersProfile():
    suffix = '/1/customers' + cid
    return requests.put(url + suffix, json=put, auth=HTTPBasicAuth(cid, passwd))

def modifyCustomer

def modifyCustomerProfile():
    suffix = "/1/customers/" + cid
    data = {
      "street": "enter street",
      "city": "enter city",
      "note": "enter note"
    }
    return requests.put(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))



