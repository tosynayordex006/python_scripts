#!/usr/bin/python

# module 

# module contains cp,dir copy, rm dir
import shutil


# module contains isdir and isfile
#import os.path

import sys

# module contains lisdir
#import os

num_args=len(sys.argv)
print("we have %s command line argument"%(num_args))

if num_args < 4:
    print("command line arguments is incorrect")
else:
    SOURCE=sys.argv[1]
    DESTINATION=sys.argv[2]
    SOURCE_TYPE=sys.argv[3]
    print("first command line argument %s"%SOURCE)
    print("first command line argument %s"%DESTINATION)
    print("first command line argument %s"%SOURCE_TYPE)
# Variable declaration
# file example 
#SRC="schema_list.txt"
#DST="/home/localhost/backups"
'''
print("The first command line argument is {}".format(SOURCE))
print("The second command line argument is {}".format(DESTINATION)) 
print("The third command line argument is {}".format(SOURCE_TYPE))
print("")

#function definition

def filecopy():
    print("Hi this is a file copy function")
    shutil.copy(SOURCE, DESTINATION)

def directory():
    print("Hi this is a directory copy function")
    shutil.copytree(SOURCE, DESTINATION)

if SOURCE_TYPE == 'f':
    print("Calling file copy function")
    filecopy()
else:
    print("Calling directory copy function")
    directory()

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
'''
