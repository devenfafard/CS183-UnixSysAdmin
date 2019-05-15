#!/usr/bin/python

import sys
import os

directory_path = os.path.dirname(os.path.realpath(__file__))
full_path = directory_path + "/log4"

log_file_exists = os.path.isfile(full_path)

if log_file_exists:
	file = open(full_path, 'r')
	lines = file.readlines()
	
	to_set = set()
	from_set = set()
	ip_set = set()
	reject_set()

	for line in lines:
		# Check for "to" addresses
		if ("to=<" in line):
			split_lines = line.split("to=<")
			fully_split = split_lines.split(">")

			if(not fully_split[0] in to_set):
				to_set.add(fully_split[0])

		# Check for "from" addresses	
		if (from=<" in line):
			split_lines = line.split("from=<")
			fully_split = split_lines.split(">")

			if(not fully_split[0] in from_set):
				from_set.add(fully_split[0])

		# Check for rejected IP addresses based on dnsbl.sorbs.net
		if ("dnsbl.sorbs.net" in line):
			split_lines = line.split("Client host [")
			fully_split = split_lines.split("]")

			if(not fully_split[0] in reject_set):
				reject_set.add(fully_split[0])"

		# Check for unique IP addresses 
		split_lines = line.split("[")
			fully_split = split_lines.split("]")
			for x in fully_split:
				print(x)
