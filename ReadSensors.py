import json
import random

from ServerRequest import *


def handleResponse(response, verbosity=1):
    if verbosity==3:
        print(response.status_code)
    if verbosity==2:
        print(response.content)
    if verbosity==1:
        print(json.dumps(response.json(), indent=4))


def readGyro():
    return random.random()

r = queryLoggedInUserAndCustomerList()
handleResponse(r)



