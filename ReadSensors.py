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


setHigherTrustLevel()
r = insertNewValuesHistoricalDataChannel()
handleResponse(r, 3)

r = querySitesBlueprint()
handleResponse(r)

r = queryYoungestRawValues()
handleResponse(r)

# 20180217142556949
# 201501011030
