#!/usr/bin/python

# module 

# module contains cp,dir copy, rm dir
import shutil


# module contains isdir and isfile
#import os.path

import sys

# module contains lisdir
#import os

SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]

# Variable declaration
# file example 
#SRC="schema_list.txt"
#DST="/home/localhost/backups"

print("The first command line argument is {}".format(SOURCE))
print("The second command line argument is {}".format(DESTINATION)) 
print("")

shutil.copytree(SOURCE, DESTINATION)


print("The source of object is : {}".format(SOURCE))
print("The destination directory is : {}".format(DESTINATION))

#copying file or directory

# checking wether source file is file or directory
#if os.path.isdir(SRC):
#    shutil.copytree(SRC, DST)
#else:
#    print(os.listdir(DST))
#    shutil.copy(SRC, DST)
#    print(os.listdir(DST))
#print("Copying object into destination folder")
#print("Object copied!")

