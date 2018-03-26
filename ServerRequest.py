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
    return requests.put(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def modifyCustomerProfile():
    suffix = '/1/customer' + cid
    put = {"street": "enter street",
           "city": "enter city",
           "note": "enter note"
           }
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def sendEmailOnBehalfThisCustomer():
    suffix = '/1/customer/' + cid + '/cn-sending/'
    post = {"receivers": [
        "person1@test.com",
        "person2@test.com"
    ],
        "subject": "Hi all - from rapidM2M!",
        "body": "<html><h1>Hi all</h1>My first message sent via rapidM2M BACKEND API</html>"
    }
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))


def modifyCustomerProfile():
    suffix = "/1/customers/" + cid
    data = {
        "street": "enter street",
        "city": "enter city",
        "note": "enter note"
    }
    return requests.get(url + suffix, json=data, auth=HTTPBasicAuth(cid, passwd))

def deleteCustomerAllHisSitesAndData():
    suffix = '/1/customer'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def sendSMSBehalfThisCostumer():
    suffix = '/1/costumer' + cid + '/cn-sendsms/'
    post = {"receivers": [
        "+4311111111",
        "+4312222222"
    ],
        "subject": "Hi all - from rapidM2M!"
    }
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#Manage a site

def queryCostomersListOfSites():
    suffix = '/1/customer' + cid + '/sites/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def querySitesBlueprint():
    suffix = '/1/customer' +cid + '/sites/' + sid + '/blueprint/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#Manage a divice

#Sites status&configuration data

def querySitesConfigurtion():
    suffix = '/1/costumer' + cid + '/sites/' + sid + '/config0/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def modifySitesConfiguration():
    suffix = '/1/customers/' + cid + '/config0/'
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#SitesTimeSeriesData

def queryYoungstRawValues():
    suffix = '/1/customer' + cid + '/sites/' + sid + '/histdata0/youngest'
    get = {
        "select": [
            "ch0",
            "ch3",
            "ch1"
        ]
    }
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def queryTimeWindowWithRawValues():
    suffix = '/1/costomers' + cid + '/sites/' + sid + '/histdata0'
    get = { "select": [
        "ch0",
        "ch3",
        "ch1"
    ],
        "from": "20150101",
        "until": "*"
    }
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

def instertNewValuesHistorialDataChannel():
    suffix = '/1/customers' + cid + '/siter/' + sid +'/histdata0'
    post = {
  "stamp": "201501011030",
  "ch0": 1,
  "myFieldName": 3.1,
  "textField": "demo_text"
}
    return requests.get(url + suffix, auth=HTTPBasicAuth(cid, passwd))

#Sites position data

def queryyoungestpositionValues():
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





















