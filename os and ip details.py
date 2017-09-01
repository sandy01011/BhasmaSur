#!/usr/bin/python
import platform
import os
import sys

######## OS TYPE AND DETAILS ##################
print ('#######################################')
print ("OS details is as follow:- ")
ostype = platform.system()
print ("Plaform Type:- ", ostype)
print ("Version:- ", platform.version())
print ("Full Detail:- ",platform.platform())
print ('#######################################')


############## hostname ####################

mach_name = os.popen('hostname')
for i in mach_name:
	print ('Hostname of your machine is :- ', i)
print('#############################################')
################## INTERFACE DETAILS ###########

if ostype == 'Windows':
	ipdetails = os.popen('ipconfig /all')
	for lines in ipdetails.readlines():
		if "IPv4" in lines:
			print (lines)
			xyz = os.popen('ipconfig /all')
			for y in xyz.readlines():
				if "adapter" in y:
					print (y)

elif ostype == 'Linux':
	red = os.popen('cat /etc/redhat-release')
	for x in red:
		print (x)
	ipdetails = os.popen('ifconfig -a')
	for line in ipdetails:
		print (line, end="")
else:
	print ('This os is not in our database')
