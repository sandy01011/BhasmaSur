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
	t = 'netstat --interface='
	q = " | grep -v Kernel | grep -v MTU | awk '{ print $3 }'"
	adapters = ifaddr.get_adapters()
	for adapter in adapters:
	#	print (type(adapters))
		print ("traffic in  " + adapter.nice_name)
		w = t+adapter.nice_name+q
		traffic_old = os.popen(w)
		for i in traffic_old.readlines():
			print ('before traffic is:-')
			print (i)
		time.sleep(3)
		traffic_new = os.popen(w)
		for j in traffic_new.readlines():
			print ('after traffic is:- ')
			print (j)
		k = int(i) - int(j)
		print ('traffic receive in last  3 second is:- ', k )
else:
	print (' This os is not our database')
