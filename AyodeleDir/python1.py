#!/bin/usr/python

# variable declaration

a=5
x=8
y="I LOVE THE NUMBER "
c=7

z="i think mike is a guru"
p,q,s=10,15,20


# main body 
# using the + (concertenate) sign 
print(y + str(x))
print("x is the variable " + str(x) + " is the value") 

#using format to print
print("The value y is: {}, and the value z is: {}".format(y,z))
print("x is the variable, and {} is the value".format(x)) 
print("the value of p is : {} , the value of q is: {}, the value of s: {}".format(p,q,s))
print("p is the variable, and {} is the value, q is the variable and {} is value, s is the variable and {} is the variable".format(p,q,s))

# using comma sign to print

print('x is the variable,',x,' is the value')

# using percent sign format 

print("The value y is: %s and the value z is: %s"%(y,z))
print("x is the variable, and %s is the value"%(x))
print("The value of p is: %s, the value of q is: %s, the value of s is: %s"%(p,q,s))
print("p is the variable, and %s is the value, q is the variable and %s is value, s is the variable and %s is the variable"%(p,q,s))
