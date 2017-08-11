#!/bin/sh

#Create audio files
pico2wave -l en-GB -w announce.wav "The following user requested to oppen the main gate"
pico2wave -l fr-FR -w name.wav "$1"

#Play files
omxplayer -o local -l jingle.mp3
omxplayer -p -o local announce.wav
omxplayer -p -o local name.wav

#Remove temporary audio files
rm announce.wav
rm name.wav

