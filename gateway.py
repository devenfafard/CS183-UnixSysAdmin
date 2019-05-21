#!/usr/bin/python

import os

directory_path = os.path.dirname(os.path.realpath(__file__))

default_gateway_path = directory_path + "/default.txt"
netstat_path = directory_path + "/netstat_log.txt"

os.system("ip -4 route list 0/0 > default.txt")

with open(default_gateway_path, 'r') as file:
	lines = file.readlines()
	for line in lines:
		first_split = line.split("default via ")
		fully_split = first_split[1].split(" ")

		default_gateway = fully_split[0]


os.system("netstat -rn >" + directory_path + "/netstat_log.txt")

with open(netstat_path, 'r') as file:
	lines = file.readlines()
	for line in lines:
		if not "UG" in line and not "Destination" in line and not "Kernel" in line:
			first_split = line.split("0.0.0.0         ")
			fully_split = first_split[1].split("   U")
			second_split = line.split("0 ")

			device = second_split[6]
			netstat = fully_split[0]

print("gateway: " + default_gateway + " netmask: " + netstat + " device: " + device)
