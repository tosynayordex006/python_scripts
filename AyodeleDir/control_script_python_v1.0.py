#!/usr/bin/python

import sys

x=sys.argv[1]
y=sys.argv[2]

print("The first command line argument: {}".format(x))
print("The second command line argument: {}".format(y)) 

#function definition 

def function():
	if x == 'scheduled':
		print("Hi the scheduled function has been called")
	else:
		print("Hi this interview function hsd been called")

#calling funtions 
if x == 'scheduled':
	print("Calling scheduled function")
	function()
else:
	print("calling the interview function")
	function()
