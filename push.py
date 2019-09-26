from time import sleep
import requests
from sense_hat import SenseHat
import datetime as dt
from common import *
sense = SenseHat()

#REPLACE XYZ WITH your nodeRed domain name
NODE_RED_POST_URI = "https://XYZ.mybluemix.net/sense-hat"

def run():
	print("running")

	t = getTimeStamp()
	print(t)
	callNodeRED({"temp":getTemp(),
                     "humidity":getHumidity(),
                     "longitude":getLongitude(),
                     "latitude":getLatitude(),
                     "elevation":getElevation(),
                     "sensorID":getSensorID(),
                     "sensorLocalTime":getTimeStamp()
                     })



def callNodeRED(args):
    	print(args)
	r = requests.post(NODE_RED_POST_URI, data = args)
	print(r.status_code)
	print(r.json())

def getTimeStamp():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")

def getTemp():
        sense.clear()

	temp = sense.get_temperature()
	sense.clear()
        bg = (0,0,0)
        c = (255,255,255)

        if (temp >= 30.00):
            print("hot!!")
            c = (255,0,0) #red
            bg = (242,231,102) #yellow
        elif (temp < 30 and temp > 15):
            print("moderate")
            c= (3,255,53) #greenw
            bg = (5,5,5) #dark grey`
        else:
            print("cold")
            c=(3,32,252)
            bg=(225,225,230)

        sense.show_message("{} {}".format(str(temp).split('.')[0],"C"), text_colour=c, back_colour=bg, scroll_speed=0.9)
        sleep(2)
        sense.clear()
	return temp

def getHumidity():
	sense.clear()
	return sense.get_humidity()

run()