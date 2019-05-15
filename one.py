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
     # length = len(lines)
     # print(str(length))
         
     for x in range(1, 61):
          quarantine_count = 0
          reject_count = 0

          for line in lines:
               # Convert characters to minute int              
               minute = (ord(line[11])*10) + ord(line[12])
               print(str(minute))
               if(minute == x):
                    if(re.search('quarantine', line)):
                         quarantine_count += 1

                    elif(re.search("reject", line)):
                         reject_count += 1

#          print("For minute " + str(minute) + ": Q = " + str(quarantine_count) + " R = " + str(reject_count))
          

     log_file.close()
