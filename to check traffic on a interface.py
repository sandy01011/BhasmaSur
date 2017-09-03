#!/usr/bin/python3
import platform
import os
import sys
import ifaddr
import time
ostype = platform.system()
print ("Plaform Type:- ", ostype)
if ostype == 'Windows':
	ipdetails = os.popen('ipconfig /all')

elif ostype == 'Linux':
	p = 'netstat --interface='
	q = " | grep -v Kernel | grep -v MTU | awk '{ print $3 }'"
	s = " netstat --interfaces | grep -v Kernel | grep -v MTU | awk '{ print $1 }' "
######################## using ifaddr module ###############################################	
	adapters = ifaddr.get_adapters()
	for adapter in adapters:
		print ("traffic in  " + adapter.nice_name)
		r = p+adapter.nice_name+q
################################################################################	

########################## without using ifadddr module ###################
	#adapters = os.popen(s)
	#for adapter in adapters:
	#	r = p+adapter+q
#############################################################################	
		traffic_old = os.popen(r)
		for i in traffic_old.readlines():
			print ('before traffic is:-')
			print (i)
		time.sleep(3)
		traffic_new = os.popen(r)
		for j in traffic_new.readlines():
			print ('after traffic is:- ')
			print (j)
		k = int(j) - int(i)
		print ('traffic receive in last  3 second is:- ', k )
		if k != 0:
			print ('The adapter which is active is:- ',adapter.nice_name)
#			print ('The adapter which is active is:- ',adapter)
else:
	print (' This os is not our database')
