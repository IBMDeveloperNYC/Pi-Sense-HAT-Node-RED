# pi-hat-node-red



## on Raspberry Pi with hat
```sh
sudo su
crontab -e
# add the following line to POST updates every 5 minutes

5 * * * * /usr/bin/python /home/pi/dev/pushSenseData/push.py >> /home/pi/sense.log 2>&1

exit
#back to pi userpw
mkdir -p /home/pi/dev/pushSenseData

```

