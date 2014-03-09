#!/bin/bash
echo "Starting eyeDoor..."
sudo /home/pi/eyedoor/application.py &
sudo rmmod uvcvideo
sudo modprobe uvcvideo
sudo motion -n &