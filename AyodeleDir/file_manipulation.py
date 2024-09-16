#!/usr/bin/python
import sys,os

#entry=raw_input("enter name: ")
'''
if (len(sys.argv)) != 2:
	print("you enetered the wrong command lie argument")
	exit()
else:
	threshold=sys.argv[1]
	print("you entered the threhold {}".format(threshold))

fh=open("emmanuel_backup.par","w+")
fh.write("I like Mike as my teacher!!")

fh.close()
fh=open("emmanuel_backup.par","r+")
file_content=fh.read()
print(file_content)
fh.close()

list=os.listdir('.')
print(list)
for x in list:
	if x =="file_manipulation.py":
		print("i found my file")

	
entry=int(raw_input("Enter disk utilization threshold: "))
print('You enetered {}'.format(entry))
'''


threshold="85%
threshold.replace('%', '')
print(threshold)
