import math
import json 
import sys
from time import sleep
from colorLetter8x8 import *
import requests
from sense_hat import SenseHat
import datetime as dt
from lookupIP import ip_meta
from getLocalPiMeta import pi_meta
from common import getElevation
import time
import argparse
import pprint

sense = SenseHat()
SCROLL_SPEED = 0.2

def getSec():
    sec = time.mktime(dt.datetime.now().timetuple())
    return sec

def run(urls, openWeatherAPIkey):
    data = {"temp":getTemp(),
                     "humidity":getHumidity(),
                     "longitude":getLongitude(),
                     "latitude":getLatitude(),
                     "elevation":getElevation(),
                     "sensorID":getSensorID(),
                     "city":getCity(),
                     "key":openWeatherAPIkey, 
                     "sensorLocalTime":getTimeStamp()}
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
    url_ = urls[0]
    print("about to POST to {}".format(url_))
    try:
        ret = requests.post(url_, json=data)
        print(ret.status_code)
        return_json_ = ret.json()
        pp.pprint(return_json_)
        #pdb.set_trace()

        msg_ = "OUTDOORS it is {} degrees celcius and {}".format(return_json_["outdoors"]["celcius"], return_json_["weather"][0]["description"])
        displayText(msg_, SCROLL_SPEED)
    except Exception as postex:
        print(postex)


def getSensorID():
    return getPiMeta()['Output']['Serial']



def getCity():
    return getMetaOffLocalPiIP()['city']

def getPiMeta():
    meta_ = pi_meta()
    return meta_

def getLatitude():
    return getMetaOffLocalPiIP()['lat']

def getLongitude():
    return getMetaOffLocalPiIP()['lon']

def getMetaOffLocalPiIP():
    """ may not be very accurate """
    return ip_meta()
    
def displayText(txt, speed):
    sense.clear()
    sense.show_message(txt , scroll_speed = speed)
    sense.clear()

def callNodeRED(url, data):
    try:
        r = None
        print("About to post to {}".format(url))
        r = requests.post(url, data = data)
        print(r.status_code)
        print(r.json())
    except Exception as rex:
        print("error")
        print(rex)

def getTimeStamp():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")

def mkLetter(C, X, O):
        sense.clear()
        if C == 'H':
            letter = letterH(X, O)
        elif C == 'M':
            letter = letterM(X, O)
        else:
            letter = letterC(X, O)

        sense.set_pixels(letter)

def getTemp():
    sense.clear()
    temp = sense.get_temperature()
    sense.clear()
    return temp

def displayTemp():
        sense.clear()

        temp = getTemp()
        sense.clear()
        bg = (0,0,0)
        c = (255,255,255)
        L = ''
        if (temp >= 30.00):
            print("hot!!")
            L='H'
            c = (255,0,0) #red
            bg = (242,231,102) #yellow
        elif (temp < 30 and temp > 15):
            print("moderate")
            L='M'
            c= (3,255,53) #greenw
            bg = (5,5,5) #dark grey`
        else:
            print("cold")
            L='C'
            c=(3,32,252)
            bg=(225,225,230)

        mkLetter(L,c,bg)
        sleep(2)
        sense.clear()

        msg_ = "{} degrees celcius".format(math.floor(temp))
        sleep(4)
        displayText(msg_, SCROLL_SPEED)
        return temp

def getHumidity():
    sense.clear()
    return sense.get_humidity()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run SenseHAT clock')
    parser.add_argument('--key', action='store', type=str, required=True)

    args = parser.parse_args()
    openWeatherKey = args.key
    print("Using api key {}".format(openWeatherKey))
    url_=["http://gmsnodered.us-south.cf.appdomain.cloud/sense-hat2"]
    
    displayTemp()

    run(url_, openWeatherKey)
