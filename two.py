#!/usr/bin/python

import sys
import os

directory_path = os.path.dirname(os.path.realpath(__file__))
full_path = directory_path + "/log22"

log_file_exists = os.path.isfile(full_path)

if log_file_exists:
	file = open(full_path, 'r')
	lines = file.readlines()

	known_dict = dict()
	unknown_dict = dict()

	for line in lines:
		if "postfix" in line:
			if " connect from unknown[" in line:
				header_split = line.split(" connect from unknown[")
				fully_split = header_split[1].split("]")

				if fully_split[0] in unknown_dict:
					unknown_dict[fully_split[0]] += 1

				else:
					unknown_dict[fully_split[0]] = 1

	
			elif " connect from " in line:	
				header_split = line.split(" connect from ")
				ip_split = header_split[1].split("[")
				fully_split = ip_split[1].split("]")

				if fully_split[0] in known_dict:
					known_dict[fully_split[0]] += 1

				else:
					known_dict[fully_split[0]] = 1

	sorted_known = sorted(known_dict.items(), key=lambda item: item[1], reverse=True)
	sorted_unknown = sorted(unknown_dict.items(), key=lambda item: item[1], reverse=True)

	for x in list(sorted_known):
		top_value_known = x[0]
		top_key_known = x[1]
		break

	for x in list(sorted_unknown):
		top_value_unknown = x[0]
		top_key_unknown = x[1]
		break;

	
	print("Total known connections: " + str(len(sorted_known)) + " - [" + top_value_known + "] accounts for " + str(top_key_known) + " connections")
	print("Total unknown connections: " + str(len(sorted_unknown)) + " - [" + top_value_unknown + "] accounts for " + str(top_key_unknown) + " connections")
