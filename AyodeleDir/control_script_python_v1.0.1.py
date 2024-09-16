#!/usr/bin/python

import shutil
import sys
import os
import os.path
import time

SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
time_string=time.localtime()
print(time_string)

TS=time.strftime("%d%m%y%M%S",time_string)
print(TS)
y=TS
z=DESTINATION + "_" + str(y)
print(z)

print("The first command line argument: {}".format(SOURCE))
print("The second command line argument: {}".format(DESTINATION)) 
print ("")

#function definition 

def f_d_copy(SOURCE,DESTINATION):
	if os.path.isdir(SOURCE):
		print("Hi, this is a directroy copy funtion")
		shutil.copytree(SOURCE,z)
		print(os.listdir(z))
	else:
		print("Hi, this is a file copy funtion")
		shutil.copy(SOURCE,DESTINATION)
		print(os.listdir(DESTINATION))

#calling funtions 
f_d_copy(SOURCE,DESTINATION)

