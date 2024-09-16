#!/usr/bin/python

import sys

x=sys.argv[1]
y=sys.argv[2]
print("The first command line argument is {}".format(x))
print("The second command line argument is {}".format(y)) 


#function definition

def scheduled():
    print ("Hi the scheduled function has been called")

def interview():
    print ("Hi the interview function has been called")

#check usage
if x == 'scheduled':
        print("Calling the scheduled function")
        scheduled()
else:
        print("Calling the interview function")
        interview()

