#!/usr/bin/python

import time
time_string=time.localtime()
print(time_string)

TS=time.strftime("%d%m%y%M%S",time_string)
print(TS)
