#!/bin/usr/python
import time
import os
import shutil
#import time

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
        "/backup/AWSJULY24/Comfort",
        "/backup/AWSJULY24/ESTHER",
        "/home/Cloudserver/scripts/mumu",
        "/home/Cloudserver/scripts/ayomide",
        "/u01/transient_files/ebenezer",
        "/u01/instantclient/ebenezer",
        "/home/Cloudserver/scripts/adisa"
        ]


def f_d_copy(source_list, destination_list):

        time_string=time.localtime()
        TS=time.strftime("%d%m%y%M%S",time_string)
        a=TS
        print(a)
        #z=destination_list + "_" + str(a)

        #if os.path.isdir(source_list):
        for source in source_list:
                for destination in destination_list:
                        #loop through the destination list to create destination directrory if it doesn't exits
                        if not os.path.exists(destination):
                                os.makedirs(destination)
                        # check if source is a directory
                if os.path.isdir(source):
                # loop through all the source file in source list
			for file_name in os.listdir(source):
			        print("Hi this is a directory copy function")
        			source_file = os.path.join(source, file_name)
        			destination_file=os.path.join(destination, file_name)
				#check if it is a file
			if os.path.isfile(source_file):
        			print("Hi this is a file copy function")
        			#copy the file into destination directory
        			shutil.copy2(source_file, destination_file)
        			print("copied file {} into {}".format(source_file,destination_file))
			elif os.path.isdir(source_file):
  			      #copy the directory into destination directory
        			if not os.path.exists(destination_file):
               				shutil.copytree(source_file, destination_file)
 		               		print("copied directory {} into {}".format(source_file,destination_file))

#shutil.copytree(x,y)
#else:

f_d_copy(source_list, destination_list)
