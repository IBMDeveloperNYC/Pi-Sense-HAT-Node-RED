import sys
import datetime as dt
from time import sleep
from json import dumps
from kafka import KafkaProducer
from sense_hat import SenseHat
from common import *
sense = SenseHat()






def getTemp():
    sense.clear()
    return sense.get_temperature()

def getHumidity():
    sense.clear()
    return sense.get_humidity()

def getDateTimeStamp():
    now = dt.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")


bootstrap_servers = ['localhost:9092']
topic = "SenseHat001"

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                        value_serializer=lambda x:
                        dumps(x).encode('utf-8'))
for e in range(3):
    data = {'sensorLocalTime':getDateTimeStamp(),'longitude':getLongitude(), 'latitude':getLatitude(), 'humidity':getHumidity(), 'temperature' : getTemp(), "elevation":getElevation(), "sensorID":getSensorID()}
    producer.send(topic, value=data)
    print(data)

    sleep(3)

sys.exit() 
