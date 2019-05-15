#!/usr/bin/python

import sys

args = sys.argv[1:]
keywords = sys.argv[2:]

with open(args[0], 'r+') as log_file:
	lines = log_file.readlines()
	log_file.seek(0)

	for line in lines:
		for word in keywords:
			if (word in line):
				# Keyword match, don't write back to file
				break
			else:
				log_file.write(line)
				
	log_file.truncate()
