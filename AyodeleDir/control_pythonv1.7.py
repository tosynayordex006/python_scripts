#!/bin/usr/python
#import time
#import os
import shutil
#import time

def f_d_copy():
	source_list = [
        	"/u02/jdk/bin",
        	"/u02/instantclient",
        	"/backup/AWSJULY24/DATAPUMP",
        	"/home/Cloudserver/scripts/appfile.txt",
        	"/home/Cloudserver/scripts/first_file.txt",
        	"/home/Cloudserver/scripts/create_tosyn_dir.sh",
        	"/home/Cloudserver/1.txt"
        ]
	destination_list = [
        	"/backup/AWSJULY24/bolusssss",
        	"/backup/AWSJULY24/blessingsssssss",
        	"/home/Cloudserver/fumnisssssss",
        	"/home/Cloudserver/scripts/folashadesssss",
        	"/u01/transient_docsssssss",
        	"/u01/instantclientsesesssssssss",
        	"/home/Cloudserver/scripts/emmassssss"
        	]

	for x in source_list:
		#x == source
		for y in destination_list:
		#y == destination
			shutil.copytree(x,y)

f_d_copy()
'''
else: 
	CONTROL_FLAG == "regular"	
'''
	
