#!/bin/usr/python

import shutil
import sys,os


def check_disk_usage(path, threshold):
    """Check if disk usage exceeds the specified threshold."""
   # total, used, free = shutil.disk_usage(path)
   # total_percent = (used / total)*100
    #print("disk utilization percentage is: {}%".format(total_percent))
    total_percent=$(df -h / | grep '/' | awk '{print $5}' | sed 's/%//')
    print("disk utilization percentage is: {}%".format(total_percent))

    if (total_percent < threshold):
        print("Maximum disk threshold already exceeded")
    else:
        print("Disk usage is within limits:used {}".format(total_percent))
if __name__ == "__main__":

    if (len(sys.argv)) != 2:
        print("you entered the wrong no of command line argument")
        sys.exit(1)

    try:
        threshold= float(sys.argv[1])
    except ValueError:
        print("Threshold must be a number")
        sys.exit(1)


    print("you entered the threhold {}".format(threshold))

         # Path to check disk usage. Change as needed.
path = "/mnt/c"

check_disk_usage(path, threshold)
                                                                        
