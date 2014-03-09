#!/bin/bash
echo "Stopping eyeDoor..."
sudo pkill -9 -f /home/pi/eyedoor/application.py
sudo /home/pi/eyedoor/motion_end.py
sudo pkill -9 motion
echo "Stopped eyeDoor"