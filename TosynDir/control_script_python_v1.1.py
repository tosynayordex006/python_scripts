#!/usr/bin/python

# module 
#from distutils.dir_util import copy_tree
# module contains cp,dir copy, rm dir
import shutil


# module contains isdir and isfile
import os.path

import sys

# module contains lisdir
import os

import time

# Variable Declaration
#print(TS)
#y=TS
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)
y=TS
z=DESTINATION + "_" + str(y)
#print(z)
#NEW_DEST=DESTINATION + "/" + SOURCE
#NEW_DEST=os.path.join(z,SOURCE)
print(z)
#NEW_DEST=os.path.join(SOURCE,z)
#print(NEW_DEST)
print("first command line argument is",SOURCE)
print("The first command line argument is {}".format(SOURCE))
print("The second command line argument is {}".format(z)) 
#print("The third command line argument is {}".format(SOURCE_TYPE))
print("")


# main body
def bk_copy(a,b):

# checking wether source file is file or directory
    if os.path.isdir(SOURCE):
        print("Hi this is a directory copy function")
        shutil.copytree(SOURCE, z)
        print(os.listdir(z))
        print("Copying %s into destination folder %s" %(SOURCE,z))
        print("Object copied!")
    #directory()
    else:
        print(os.listdir(DESTINATION))
        print("Hi this is a file copy function")
        shutil.copy(SOURCE, DESTINATION)
#       filecopy()

        print(os.listdir(DESTINATION))
        print("Copying object into destination folder")
        print("Object copied!")

bk_copy(SOURCE,DESTINATION)

