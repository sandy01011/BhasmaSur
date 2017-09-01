#!/usr/bin/python
import platform
import os
import sys
import ifaddr

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
for i in mach_name.readlines():
	print ('Hostname of your machine is :- ', i)
print('#############################################')

################## INTERFACE DETAILS ########################

if ostype == 'Windows':
	ipdetails = os.popen('ipconfig /all')
	for lines in ipdetails.readlines():
		if "IPv4" in lines:
			print (lines)
#			xyz = os.popen('ipconfig /all')
#			for y in xyz.readlines():
#				if "adapter" in y:
#					print (y)

elif ostype == 'Linux':
	red = os.popen('cat /etc/redhat-release')
	for x in red:
		print (x)
#	ipdetails = os.popen('ifconfig -a')
#	for line in ipdetails:
#		print (line, end="")
else:
	print ('This os is not in our database')


###################### Interface and ip details using ifaddr module #############################

print ('############################################')
adapters = ifaddr.get_adapters()

for adapter in adapters:
	print ("IPs of network adapter " + adapter.nice_name)
	for ip in adapter.ips:
		print ("   %s/%s" % (ip.ip, ip.network_prefix))
		
##########################################################################################
