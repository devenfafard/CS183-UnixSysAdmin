#!/usr/bin/python

import sys

args = sys.argv[1:]

to_dict = dict()
from_dict = dict()

for arg in args:
	log_file = open(arg, 'r')
	lines = log_file.readlines()

	for line in lines:
		if("to=<" in line):	
                	split_lines = line.split("to=<")
			fully_split = split_lines[1].split(">")

			if(fully_split[0] in to_dict):				
				to_dict[fully_split[0]] += 1
			else:
				to_dict[fully_split[0]] = 1

		elif("from=<" in line):
			split_lines = line.split("from=<")
			fully_split = split_lines[1].split(">")

			if(fully_split[0] in from_dict):
				from_dict[fully_split[0]] += 1
			else:
				from_dict[fully_split[0]] = 1
		
	print("****** Top 5 To Addresses *****")	
	sorted_to = sorted(to_dict.items(), key=lambda item: item[1], reverse=True)
	for x in list(sorted_to)[0:5]:
		print(x)

	print("***** Top 5 From Addresses ******")
	sorted_from = sorted(from_dict.items(), key=lambda item: item[1], reverse=True)
	for x in list(sorted_from)[1:6]:
		print(x)
