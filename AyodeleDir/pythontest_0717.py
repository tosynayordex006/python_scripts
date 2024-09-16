#!/usr/bin/python

import time 
import commands
import random

x="stupid"

def test_global():
    global x
    x="fantastic"

    print("python is: %s"%(x))

test_global()

print("python is: %s"%(x))

# check data type of a variable
print("type: %s"%(x))

# Differnt data set types

# create tuple
check_tuple=("mike", "tom", "cindy")
print(check_tuple)
'''
check_tuple[0]="shola"
print(check_tuple)
'''
print(check_tuple[2])


# create list
fruit_list=["apple", "banna", "cherry"]
print(fruit_list)

for x in fruit_list:
	print(x)


# Create dictionary
student={
	"student_fname":"Tom",
	"student_lname":"smith",
	"gender":"M"
	}

print(student)

# for loops in dictionary listing

for x in student:
	print(x)
	print(student[x])


cars={
	"brand":[{"main_brand":"Audit", "sub_brand":"Porsche"},{"main_brand":"Audit", "sub_brand":"A7"}],
	"model":"Panamera",
	"year":"1996",
	}

print(cars["brand"][1]["sub_brand"])

print(random.randrange(1,10))

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)
print("starting code run at %s"%(TS))

hostname=commands.getoutput('hostname')
print("the hostname is %s"%(hostname))


word="print"
print(word[2])
print(word[-1])
print(word[2:])
print(len(word))


cube=[1,8,27,81]
cube[2:]=[]
print(cube)
