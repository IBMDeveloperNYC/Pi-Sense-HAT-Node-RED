import sys
from time import sleep
from colorLetter8x8 import *
import requests
from sense_hat import SenseHat
import datetime as dt
from common import *
sense = SenseHat()

def run(url):
    print("running")

    t = getTimeStamp()
    print(t)
    callNodeRED(url, {"temp":getTemp(),
                     "humidity":getHumidity(),
                     "longitude":getLongitude(),
                     "latitude":getLatitude(),
                     "elevation":getElevation(),
                     "sensorID":getSensorID(),
                     "sensorLocalTime":getTimeStamp()
                     })




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
        sleep(7)
        sense.clear()
        sense.show_message("{} {}".format(str(temp).split('.')[0],"C"), text_colour=c,  scroll_speed=0.9)
        sleep(2)
        mkLetter(L,c,bg)
        sleep(7)
        sense.clear()
        return temp

def getHumidity():
    sense.clear()
    return sense.get_humidity()

if __name__ == '__main__':
    urlEg_ = "https://<<yourNodeRedSubDomainname>>.mybluemix.net/<<your-end-point-path>>"
    if len(sys.argv) != 2:
        print("pass url to post data to, e.g. {}".format(url-eg))
    else:
        url_ = sys.argv[1]

        run(url_)
