#!/bin/bash
if [ "$1" == "START" ];
then
	sudo /home/pi/eyedoor/motion_start.py &
else
	sudo /home/pi/eyedoor/motion_end.py &
fi