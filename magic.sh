#!/bin/bash

find /usr/src/kernels -type f -name "*.h" -exec grep -i magic {} \; | wc -l


#####
#find [@folder], -name [files w/ .h ext] -exec [grep to find keyword, -i ignore case] "magic"
