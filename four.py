#!/usr/bin/python

import sys
import os

directory_path = os.path.dirname(os.path.realpath(__file__))
full_path = directory_path + "/log4444"

log_file_exists = os.path.isfile(full_path)

if log_file_exists:
	file = open(full_path, 'r')
	lines = file.readlines()
	
	to_set = set()
	from_set = set()
	ip_set = set()
	total_rejects = 0

	for line in lines:
		if " blocked using dnsbl.sorbs.net;" in line:
			total_rejects += 1

			# Parse for IP addresses
			if " Client host [" in line:
				split_lines = line.split("Client host [")
				fully_split = split_lines[1].split("]")

				if not fully_split[0] in ip_set:
					ip_set.add(fully_split[0])

			# Parse for from address
			if " from=<" in line:
				split_lines = line.split("from=<")
				fully_split = split_lines[1].split(">")

				if(not fully_split[0] in from_set):  	
					from_set.add(fully_split[0])

			# Check for "to" addresses
			if ("to=<" in line):
				split_lines = line.split("to=<")
				fully_split = split_lines[1].split(">")

				if(not fully_split[0] in to_set):
					to_set.add(fully_split[0])

	print(str(total_rejects) + " messages rejected")
	print(str(len(ip_set)) + " unique IP's")
	print(str(len(from_set)) + " unique from addresses")
	print(str(len(to_set)) + " unique to addresses")
	
