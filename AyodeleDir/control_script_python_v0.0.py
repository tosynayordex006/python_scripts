#!/usr/bin/python

#Modules

import shutil

# variable declaration

SOURCE="/home/Cloudserver/scripts/first_file.txt"
DESTINATION="/home/Cloudserver/scripts/practicedir_favour_aprill24"

print("The source file is: {}" .format(SOURCE))
print("The source file is: {}" .format(DESTINATION))

shutil.copy(SOURCE, DESTINATION)
