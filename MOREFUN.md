### addional challenges

### SSH to your Pi 

( reminder to ssh to your pi make sure you add an empty file called `ssh` to the root of the files you copy to your ssd card )
How?  

```bash
cd << to root of the  folder you downloaded from NOOBS >>
touch ssh
stat ssh
# you should have the file needed by pi to allow ssh into the Pi
```

Now, say you don't want to wire up a keyboard, mouse and HDMI monitor ( that's a hassle 
and often not practical )

just connect a ethernet cable and power up your pi!

#### How to find the ip address of your PI

Use `nmap` a handy program that runs on max/linux ( not sure about windows? )

Installation:
Mac:
``` sh
brew instal nmap
```
RedHat/CentOS Linux:
``` sh
sudo yum install nmap
#learn more about nmap
man nmap
```

> note: don't run this at work, it could upset the network security team, nmap is:
> `Network exploration tool and security / port scanner`

Check your local ip address

```sh
ifconfig
# in my case I looked at the output and figured out that my IP is
#192.168.1.8

#so I can scan my network and find all the devices that are on it
# note the 8 is replaced with a Zero!
nmap -sn 192.168.1.0/24

#output example is
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-18 21:41 EST
Nmap scan report for RAC2V1S (192.168.1.1)
Host is up (0.0038s latency).
Nmap scan report for jackBlacksiPhone (192.168.1.4)
Host is up (0.11s latency).
Nmap scan report for LaurusNobilis (192.168.1.8)
Host is up (0.00052s latency).
Nmap scan report for Galaxy-Tab-S5e (192.168.1.31)
Host is up (0.038s latency).
Nmap scan report for raspberrypi (192.168.1.32)
Host is up (0.0024s latency).
Nmap done: 256 IP addresses (5 hosts up) scanned in 3.92 seconds
```
Great!  my ip address for my raspberrypi is 192.168.1.32

so let me ssh in from my laptop terminal

```sh
ssh pi@192.168.1.32
pi@192.168.1.32's password:
<<enter your password you used to setup your pi - raspberry is the default and you shoud change that!>>

#once in you should see
Linux raspberrypi 4.19.75-v7+ #1270 SMP Tue Sep 24 18:45:11 BST 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Dec 18 20:17:11 2019
pi@raspberrypi:~ $
```

#### adding location to the PI
based on your IP address of your pi, assuming you are not behind a large VPN/Office network you should be able to get a reasonable city or longitude or latitude.


#### get the outside weather information, by querying a free weather service with location 