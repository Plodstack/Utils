#!/bin/sh

echo startingup
sleep 120
rm -rf /run/user/1000/openports.txt
netstat -t state established > /run/user/1000/openports.txt

while :
do
# rm -rf /openports.txt
netstat -t state established > /home/pi/openports.txt

	if grep -q "piBack:30005" /home/pi/openports.txt; then
		echo connected to piBack
		sleep 120
	else
		echo not connected to piBack
		killall nc
		nc piBack 30005 | nc localhost 30004 &
		sleep 120
	fi
done
