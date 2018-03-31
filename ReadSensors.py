import json
import random
import smbus
import time

from ServerRequest import *

bus = smbus.SMBus(1)
operational = False

def __init__():
    try:
        time.sleep(0.5)
        bus.write_byte(0x40, 0xF5)
        time.sleep(0.5)
        bus.write_byte(0x40, 0xF3)
        operational = True
    except:
        pass


def getPressure():
    if operational:
        try:
            data = bus.read_i2c_block_data(0x60, 0x04, 8)
            A0 = (data[0] * 256 + data[1]) / 8.0
            B1 = (data[2] * 256 + data[3])
            if B1 > 32767:
                B1 -= 65536
            B1 = B1 / 8192.0
            B2 = (data[4] * 256 + data[5])
            if B2 > 32767:
                B2 -= 65535
            B2 = B2 / 16384.0
            C12 = ((data[6] * 256 + data[7]) / 4) / 4194304.0
            bus.write_byte_data(0x60, 0x12, 0x00)
            time.sleep(0.5)
            data = bus.read_i2c_block_data(0x60, 0x00, 4)
            pres = ((data[0] * 256) + (data[1] & 0xC0)) / 64
            temp = ((data[2] * 256) + (data[3] & 0xC0)) / 64
            presComp = A0 + (B1 + C12 * temp) * pres + B2 * temp
            pressure = (65.0 / 1023.0) * presComp + 50
            return pressure
        except:
            return -1
    return -1

def getHumidity():
    if operational:
        try:
            time.sleep(0.5)
            data0 = bus.read_byte(0x40)
            time.sleep(0.5)
            data1 = bus.read_byte(0x40)
            humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
            return humidity
        except:
            return -1
    return -1


def getTemperature():
    if operational:
        try:
            time.sleep(0.5)
            data0 = bus.read_byte(0x40)
            time.sleep(0.5)
            data1 = bus.read_byte(0x40)
            cTemp1 = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
        except:
            pass
        try:
            bus.write_byte_data(0x60, 0x12, 0x00)
            time.sleep(0.5)
            data = bus.read_i2c_block_data(0x60, 0x00, 4)
            temp = ((data[2] * 256) + (data[3] & 0xC0)) / 64
            cTemp2 = (temp - 498) / (-5.35) + 25
        except:
            pass
        if cTemp1 is not None and cTemp2 is not None:
            return (cTemp1+cTemp2)/2
        elif cTemp1 is not None:
            return cTemp1
        elif cTemp2 is not None:
            return cTemp2
        else:
            return -1
    return -1





def handleResponse(response, verbosity=1):
    if verbosity==3:
        print(response.status_code)
    if verbosity==2:
        print(response.content)
    if verbosity==1:
        print(json.dumps(response.json(), indent=4))
        # print(response.content)




setHigherTrustLevel()
r = insertNewValuesHistoricalDataChannel()
handleResponse(r, 3)

r = querySitesBlueprint()
handleResponse(r)

r = queryYoungestRawValues()
handleResponse(r)
handleResponse(r, 3)

# 20180217142556949
# 201501011030
