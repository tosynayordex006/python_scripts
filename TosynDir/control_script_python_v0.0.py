#!/usr/bin/python

#Modules
import shutil

# Variable declaration 

SOURCE="/home/localhost/scripts/first_file.txt"
DESTINATION="/home/localhost/scripts/practicedir_tosyn_aprill24/backup"


print("the source file is: {}" .format(SOURCE))
print("the Destination directory is: {}" .format(DESTINATION))


shutil.copy(SOURCE, DESTINATION)
