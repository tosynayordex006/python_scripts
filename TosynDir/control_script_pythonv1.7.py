#!/bin/usr/python

import shutil
import sys,os


def check_disk_usage(path, threshold):
    """Check if disk usage exceeds the specified threshold."""
    total, used, free = shutil.disk_usage(path)
    total_percent = (used / total)*100
    print("disk utilization percentage is: {}%".format(total_percent))


    if (total_percent < threshold):
        print("Maximum disk threshold already exceeded")
    else:
        print("Disk usage is within limits:used {}".format(total_percent))
if __name__ == "__main__":
    # Path to check disk usage. Change as needed.
    path = "/mnt/c"
    # Threshold for disk usage percentage
    threshold = 75
    print("You entered %s as threshold"%(threshold))

check_disk_usage(path, threshold)
                                                                        
