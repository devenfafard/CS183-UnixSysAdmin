#!/usr/bin/python

import sys
import os

# Check to see if hourlyInfo.txt exists. If not, 
# create it in the current directory.

directory_path = os.path.dirname(os.path.realpath(__file__))
full_path = directory_path + "/hourlyInfo.txt"

hourly_info_exists = os.path.isfile(full_path)

if hourly_info_exists:
     print("********** hourlyInfo.txt found! **********\n")
     output_file = open(full_path, "r+")

else:
     print("********** creating hourlyInfo.txt! **********\n")
     output_ = open("hourlyInfo.txt", "w+")

# Get log file from command line arguments and throw the lines into an array

args = sys.argv[1:]

for arg in args:
     log_file = open(arg, "r")
     lines = log_file.readlines()

     for line in lines:
          print(line[11])
          

     f.close()

# For each line in hourlyInfo.txt, parse lines matching each minute
# If they contain the word 'quarantine' or 'reject' increment a counter

quarantine_count = 0
reject_count = 0
minute_count = 0; 
