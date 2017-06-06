#!/bin/sh

# run linphone deamon
printf "Init linphone...\n"
linphonecsh init -c ~/.linphonerc

sleep 1

# make call
printf "Make call...\n"
linphonecsh generic "call 06xxxxxxxx@sip3.ovh.fr"

#wait 8 second (time to receive the call on the other side)
sleep 8
echo sleep

# terminate call
printf "Terminate call... \n"
linphonecsh generic "terminate"
#echo terminate call

sleep 1

#exit linphone deamon
linphonecsh exit
printf "Exit linphone... \n"

exit

