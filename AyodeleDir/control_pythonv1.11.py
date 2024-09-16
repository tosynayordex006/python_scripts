#!/bin/usr/python

import psutil

def check_disk_usage(path="/", threshold=75):
    """Check if disk usage exceeds the specified threshold."""
    total, used, free = psutil.disk_usage(path)
    total_percent = (used / total) * 100
    
    if total_percent > threshold:
        print("Maximum disk threshold already exceeded")
    else:
        print("Disk usage is within limits: {total_percent:.2f}% used")

if __name__ == "__main__":
    # Path to check disk usage. Change as needed.
    path = "/"
    
    # Threshold for disk usage percentage
    threshold = 75
    
    check_disk_usage(path, threshold)
