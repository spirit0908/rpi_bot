#/bin/sh

#Intercom door button connected to pin 29 of raspberry pi (via relay)
pin=29

#Set pin to output mode
/usr/local/bin/gpio mode $pin out
sleep 1

#Trigger door opening for 5sec
/usr/local/bin/gpio write $pin 1
sleep 5

#Stop trigger
/usr/local/bin/gpio write $pin 0

