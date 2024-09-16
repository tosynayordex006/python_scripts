#!/bin/usr/python

import shutil

# Variable declaration 

SOURCE="/home/Cloudserver/scripts/first_file.txt"
DESTINATION="/home/Cloudserver/scripts/mumu"

print("the source file is: {}".format(SOURCE))
print("the destination folder is: {}".format(DESTINATION))

shutil.copy(SOURCE, DESTINATION)
print("file {} successfully copied into destination {}".format(SOURCE,DESTINATION))
