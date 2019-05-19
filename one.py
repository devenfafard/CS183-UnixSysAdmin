#!/usr/bin/python

import sys
import os
import re

# Check to see if hourlyInfo.txt exists. If not, 
# create it in the current directory.

directory_path = os.path.dirname(os.path.realpath(__file__))
full_path = directory_path + "/hourlyInfo.txt"

hourly_info_exists = os.path.isfile(full_path)

if hourly_info_exists:
	output_file = open(full_path, "r+")

else:
	output_file = open("hourlyInfo.txt", "w+")

args = sys.argv[1:]

for arg in args:
	log_file = open(arg, 'r')
	lines = log_file.readlines()

	for x in range(1, 60):
		quarantine_count = 0
		reject_count = 0

		for line in lines:
			if ":" in line:
				split_line = line.split(":")
				minute = int(split_line[1], 10)

				if minute == x:
					if "postfix" in line and "reject" in line:
						reject_count += 1

					if "amavis" in line and "quarantine" in line:
						quarantine_count += 1 
			
		output_file.write("Mar 1 00:" + str(x) + " [postfix rejects:" + str(reject_count) + "] [amavis quarantines:" + str(quarantine_count) + "]")
		output_file.write("\n")
   

	log_file.close()
