#!/usr/bin/python

import sys

source=sys.argv[1]
destination=sys.argv[2]

print("the first command line argument is {}".format(source))
print("second command line argument is {}".format(destination))
print("")
#function defimation
def scheduled():
	print("Hi the scheduled functio has been called")

if source == "scheduled":
	print("calling the scheduled function")
	scheduled()
else:
	print("calling the interview function")
