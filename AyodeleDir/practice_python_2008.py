#!/usr/bin/python
import os
'''
def check_word():
	a="Yello Cloud Engineers"
	if a[0] == "H":
		print("The first letter of the word is %s"%(a[0]))
	else:
		print("The remaining letter of the word are %s"%(a[1:]))
check_word()


fh=open("practice_python_2008.log","w+")
fh.write("I love Cloud Engineering!!!")

fh.close()
fh=open("practice_python_2008.log","r+")
file_content=fh.read()
print(file_content)
fh.close

for x in os.listdir('.'):
	if x == "practice_python_2008.log":
		print(x)

		fh=open(x,"r+")
		file_content=fh.read()
		print(file_content)
		fh.close
	else:
		print("The file is not found")



threshold="85%"
threshold=threshold.replace('%', '')
print(threshold)
threshold="95%"
threshold=threshold.strip('%')
print(threshold)


a="MUNZER"
print(a.lower())

a="munzer"
print(a.upper())


for x in os.listdir('.'):
        if x == "practice_python_2008.log":
                print(x)

                fh=open(x,"r+")
                file_content=fh.read()
                print(file_content)
		file_content=file_content.replace('Engineering', 'Business')
		print(file_content)
		fh.close

fh=open("practice_python_2008.log","r+")
file_content=fh.read()
print(file_content)
fh=open("practice_python_2008.log","w+")
file_content=file_content.replace('Business', 'Engineering')
fh.write(file_content)
print(file_content)
fh.close
'''

work_dir=os.getcwd()
#print(work_dir)
workdir_new=work_dir.split('/')
print(workdir_new[1])
print(workdir_new[2])
print(workdir_new[3])
print(workdir_new[4])





