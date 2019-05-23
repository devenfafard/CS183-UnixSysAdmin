#!/usr/bin/python

import os
import sys
import math

args = sys.argv[1:]
subnet_mask = [0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,]

for arg in args:
	netmask_bits= int(arg, 10)
	num = 32 - netmask_bits
	num_hosts = pow(2, num)
	num_usable = num_hosts - 2

	# Add number of 1's to subnet mask
	for x in range(0, netmask_bits):
		if(subnet_mask[x] == 0):
			subnet_mask[x] += 1

	first_octet =[]
	for x in range(0, 8):
		first_octet.append(str(subnet_mask[x]))
	firstoct_str = ''.join(first_octet)
	firstoct_int = int(firstoct_str, 2)	
	
	second_octet = []
	for x in range(8, 16):
		second_octet.append(str(subnet_mask[x]))
	secondoct_str = ''.join(second_octet)
	secondoct_int = int(secondoct_str, 2)	

	third_octet = []
	for x in range(16, 24):
		third_octet.append(str(subnet_mask[x]))
	thirdoct_str = ''.join(third_octet)
	thirdoct_int = int(thirdoct_str, 2)	

	fourth_octet = []
	for x in range(24, 32):
		fourth_octet.append(str(subnet_mask[x]))
	fourthoct_str = ''.join(fourth_octet)
	fourthoct_int = int(fourthoct_str, 2)	

	print("addresses: " + str(num_hosts) + " usable: " + str(num_usable) + 
              " netmask: " + str(firstoct_int) + "." + str(secondoct_int) + "." +
              str(thirdoct_int) + "." + str(fourthoct_int))
