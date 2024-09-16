#!/usr/bin/python

# VAriable declaration

a,b=5,"I LOVE the number"
x=5
y="I LOVE the number" 
c=7
#z=" Is the variable"
#a=" is the value"
z="I think mike is a guru"
p,q,s=10,15,20

# main body
# Using the + sign
#print(y + str(x) )
#print("x" + z,str(x) + a)
print ("x is the variable " + str(x) + " is the value")
print("the value of y is:" +y+ " and the value of c is:" + str(c))
# Using formst
print("The value of y is: {}, and the value of z is: {}".format(y,z))
print("x is the variable, and {} is the value".format(x))
print("The value of p is: {}, the value of q is: {}, the value of s is: {}".format(p,q,s))
print("p is the variable, and {} is the value. q is the variable, and {} is the value. s is the variable, and {} is the value" .format(p,q,s))
#print("q is the variable, and {} is the value".format(q))
#print("s is the variable, and {} is the value".format(s))
print("{} {}".format(b,a))

# USing comma
print('x is the variable,',x,' is the value')

#Using percent sign format and plus 
print("x is the variable, %s is the value"%x)
print("The value of x is: %s and The value of c is: %s "%(x,c)) 
print("The value of p is: %s, the value of q is: %s, the value of s is: %s"%(p,q,s))
print("p is the variable, and %s is the value. q is the variable, and %s is the value. s is the variable, and %s is the value"%(p,q,s))

print("%s %s"%(b,a))
