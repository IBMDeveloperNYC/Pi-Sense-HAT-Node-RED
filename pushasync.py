import asyncio
import sys
from time import sleep
from colorLetter8x8 import *
import requests
from sense_hat import SenseHat
import datetime as dt
from CsvHelper import CsvReader as ch

lol = ch().readCSV("./utils/users.csv")
from common import *
import time

sense = SenseHat()

def getSec():
    sec = time.mktime(dt.datetime.now().timetuple())
    return sec

def run(urls):
    t = getTimeStamp()
    start = getSec()

    for url in urls:
        print("about to call url")
        print(url)

        callNodeRED(url, {"temp":getTemp(),
                     "humidity":getHumidity(),
                     "longitude":getLongitude(),
                     "latitude":getLatitude(),
                     "elevation":getElevation(),
                     "sensorID":getSensorID(),
                     "sensorLocalTime":getTimeStamp()
                     })

    end = getSec()
    timeran = end - start
    print("script took {} seconds".format(timeran))
    displayText("{}".format(timeran))

def displayText(txt):
    sense.clear()
    sense.show_message(txt)
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
        return temp

def getHumidity():
    sense.clear()
    return sense.get_humidity()

def createUrls(lol, urlList):
    """ create urls off list of lists from users.csv"""

    for user in lol:
        firstName = user[0].strip()
        lastName = user[1].strip()
        url = "http://{}{}nodered.myblumeix.net/sense-hat".format(firstName[0].lower(), lastName[0].lower())
        urlList.append(url)
    return urlList

if __name__ == '__main__':

    url_ = ["http://pmistrynoderedtest.mybluemix.net/sense-hat"]

    try:
        lol = ch().readCSV("./utils/users.csv")
        lol = createUrls(lol, url_)

    except FileNotFoundError:
        pass

    displayTemp()

    run(url_)
