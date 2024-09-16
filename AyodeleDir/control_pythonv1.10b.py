#!/bin/usr/python

# To check if disk utilization excceed threshold

if df -h / | egrep [/] | awk '{print $5}' | sed 's/%//':
	print("Maximum disk threshold already exceeded")
else:
	print("disk threshold not exceeded")
