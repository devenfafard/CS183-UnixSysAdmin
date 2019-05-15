#!/usr/bin/python

import sys

args = sys.argv[1:]
keywords = sys.argv[2:]

with open(args[0], 'r+') as log_file:
	lines = log_file.readlines()
	log_file.seek(0)	
	log_file.truncate()

	for line in lines:
		found = False
		for word in keywords:
			if (word in line):
				# Keyword match, don't write back to file
				found = True
				break
		if (not found):
			print("Line should be in file")
			log_file.write(line)
