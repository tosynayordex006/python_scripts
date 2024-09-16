#!/bin/usr/python

import sys 
import os
import time

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)

source=sys.argv[1]
file_name=sys.argv[2]

source_file = os.path.join(source, file_name, TS)
print(source_file)
