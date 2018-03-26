import requests
from requests.auth import HTTPBasicAuth
from credential import *


permission = False

def requiresHigherTrustLevel():
    global permission
    if permission:
        permission = False
    else:
        raise PermissionError("Has to enable trust.")

def setHigherTrustLevel():
    global permission
    permission = True

#The first thing upon user login
def queryLoggedInUserAndCustomerList():
    suffix = '/1/me'
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))

#Manage a customer
def queryTheUsersCustomerList():
    suffix = '/1/customers'
    return requests.get(url+suffix,auth=HTTPBasicAuth(cid, passwd))

def addNewCustomer():
    requiresHigherTrustLevel()
    suffix  = '/1/customers'
    data = {
        "name": "enter name",
        "street": "enter street",
        "city": "enter city",
        "note": "enter note"
    }
    return requests.post(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def queryCustomersProfile():
    suffix = '/1/customers' + cid
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def modifyCustomerProfile():
    requiresHigherTrustLevel()
    suffix = '/1/customer' + cid
    data = {"street": "enter street",
           "city": "enter city",
           "note": "enter note"
           }
    return requests.put(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def sendEmailOnBehalfThisCustomer():
    requiresHigherTrustLevel()
    suffix = '/1/customer/' + cid + '/cn-sending/'
    data = {"receivers": [
        "person1@test.com",
        "person2@test.com"
    ],
        "subject": "Hi all - from rapidM2M!",
        "body": "<html><h1>Hi all</h1>My first message sent via rapidM2M BACKEND API</html>"
    }
    return requests.post(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def deleteCustomerAllHisSitesAndData():
    suffix = '/1/customer'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def sendSMSBehalfThisCostumer():
    requiresHigherTrustLevel()
    suffix = '/1/costumer' + cid + '/cn-sendsms/'
    data = {"receivers": [
        "+4311111111",
        "+4312222222"
    ],
        "subject": "Hi all - from rapidM2M!"
    }
    return requests.post(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

#Manage a site

def queryCustomersListOfSites():
    suffix = '/1/customer' + cid + '/sites/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def querySitesBlueprint():
    suffix = '/1/customer' +cid + '/sites/' + sid + '/blueprint/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#Manage a device

#Sites status&configuration data

def querySitesConfiguration():
    suffix = '/1/costumer' + cid + '/sites/' + sid + '/config0/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def modifySitesConfiguration():
    suffix = '/1/customers/' + cid + '/config0/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#SitesTimeSeriesData

def queryYoungestRawValues():
    suffix = '/1/customer' + cid + '/sites/' + sid + '/histdata0/youngest'
    data = {
        "select": [
            "ch0",
            "ch3",
            "ch1"
        ]
    }
    return requests.get(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def queryTimeWindowWithRawValues():
    suffix = '/1/costomers' + cid + '/sites/' + sid + '/histdata0'
    data = { "select": [
        "ch0",
        "ch3",
        "ch1"
    ],
        "from": "20150101",
        "until": "*"
    }
    return requests.get(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def insertNewValuesHistoricalDataChannel():
    suffix = '/1/customers' + cid + '/siter/' + sid +'/histdata0'
    data = {
        "stamp": "201501011030",
        "ch0": 1,
        "myFieldName": 3.1,
        "textField": "demo_text"
    }
    return requests.post(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

#Sites position data

def queryYoungestPositionValues():
    suffix = '/1/customer' + cid + '/sites/' + sid + '/pos/youngest/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#Manage users

def queryUserList():
    suffix = '/1/users'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def queryCustomersUserList():
    suffix = '/1/customer' + cid + '/users/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def queryUsersProfile():
    suffix = '/1/custeromers/' + cid + '/users/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))
