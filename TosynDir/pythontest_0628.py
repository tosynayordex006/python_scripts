#:!/usr/bin/python

import time
import logging
import subprocess 
import random 

#Varibale declaration

x="stupid"

def test_global():
   # global x
    x="fantastic"

    print("python is: %s"%(x))
     
test_global()

print("python is: %s"%(x))

# check data type of a variable
print(type (x))

# Differnt data set types 

# create tuple 
check_tuple=("mike", "tom", "cindy")
print(check_tuple)
check_tuple[0]="shola"
print(check_tuple)

print(check_tuple[2])

'''

#create list
fruit_list=["apple", "bananna", "cherry"]
print(fruit_list)

fruit_list[2]="plum"
print(fruit_list)


for x in fruit_list:
    print(x)

# create dictionary
student={
        "student_fname":"Tom",
        "student_lname":"Smith",
        "gender":"M"
        }
print(student)

# for loops in dictionary listing

for x in student:
    print(x)

for x in student:
    print(student[x])

print(student["student_fname"])
print(student["student_lname"])
print(student["gender"])



cars={
    "brand":{"main_brand":"Audit", "sub_brand":"Porsche"},
    "model":"Panamera",
    "year":"1964",
    }
print(cars)

print(cars["brand"]["main_brand"])

#array dictionary


cars={
        "brand":[{"main_brand":"Audit", "sub_brand":"Porsche"},{"main_brand":"Audit", "sub_brand":"A7"}],
                                       0                                    1
       "model":"Panamera",
        "year":"1964",
    }


print(cars["brand"][1]["sub_brand"])



#print(random.randrange(1,10))
word="print"
print(word[0])
print(word[-1])
print(word[-2])
print(word[0:3])
print(word[2:])

logging.basicConfig(level=logging.INFO)



#logging.basicConfig(filename='python.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)

logging.info("starting code run at %s"%(TS))

hostname=subprocess.getoutput('hostname')
logging.info ("The hostname is %s"%(hostname))

servers={
        "WINDOWS-URLDJ5Q":"patchprod"
    }

def patchprod():
    logging.info("This is the patchprod function")

if hostname in servers:
    logging.info("calling the "+servers[hostname]+" function" )
    
    if servers[hostname] == "patchprod":
     patchprod()

else:
    logging.error("specified server does not exit")
        


# differnt log levels error , info


time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)

logging.info("ending code run at %s"%(TS))

#Slicing
word="CloudEngineering"
print(word[11:])
print(word[-5:])
print(len(word))

squares=[1, 4, 9, 16, 25]
print(squares[0])
print(squares[2])
print(squares[-2:])
print(squares[-3:])
print(squares[0:3]) 
squares[-2:]=[]
print(squares)

cube=[1, 8, 27, 64]
print(squares + cube)
'''
