#!/bin/sh

echo starting up
retries=0

while :

do

packet_loss=$(ping -c 5 -q 192.168.1.29 | grep -oP '\d+(?=% packet loss)')

if [ $packet_loss -lt 100 ]
	then
		echo computer appears to respond to ping
		exit 0

	else
  		echo not responding to ping - wake it
		/usr/bin/wakeonlan C0:B5:D7:D5:C8:$D
		retries=$((retries+1))
		echo $retries
		if [ $retries -gt 10 ]
			then
			/usr/bin/python3 /home/pi/alert_bot.py -t "piFront couldn't wake the desktop up."
			exit 0
		fi
fi

done