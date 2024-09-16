#!/usr/bin/python
import os
import sys
import shutil
import os.path
import time


source=sys.argv[1]
destination=sys.argv[2]
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)
print(TS)
y=TS
new_dest=os.path.join(destination, y)
print(new_dest)

print("the first command line argument is {}".format(source))
print("second command line argument is {}".format(destination))
print("")
#function defimation
def scheduled():
	print("Hi this is file_directory copy")
	print("")
	# checking if source is file or directory
	if os.path.isdir(source):
		print("calling directory copy function")
		shutil.copytree(source, new_dest)
		print("{} directory successfully copied in destination {} directory".format(source,new_dest))
		print(os.listdir(destination))
	else:
		print("calling file copy function")
		print(os.listdir(destination))
		shutil.copy(source, destination)
		print("{} file successfully copied in destination {} directory".format(source,destination))
		print(os.listdir(destination))
# calling the function definnation
scheduled()
