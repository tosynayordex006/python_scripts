import time
import os
import shutil
import sys

def f_d_copy(source_list, destination_list):
    time_string = time.localtime()
    TS = time.strftime("%d%m%y%M%S", time_string)
    print("Timestamp:", TS)

    for source, destination in zip(source_list, destination_list):
        # Ensure destination directory exists
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Check if source is a file or directory
        if os.path.isfile(source):
            # Copy the file to the destination
            shutil.copy2(source, destination)
            print("Copied file {} to {}".format(source, destination))
        elif os.path.isdir(source):
            # Copy the directory to the destination
		dest_dir = os.path.join(destination, os.path.basename(source))
		if not os.path.exists(dest_dir):
                	shutil.copytree(source, dest_dir)
                	print("Copied directory {} to {}".format(source, dest_dir))
		else:
                	# Copy contents of the directory if it already exists
			for item in os.listdir(source):
                		source_item = os.path.join(source, item)
                		dest_item = os.path.join(dest_dir, item)
			if os.path.isdir(source_item):
                        	shutil.copytree(source_item, dest_item)
                        	print("Copied directory {} to {}".format(source_item, dest_item))
			else:
                         	shutil.copy2(source_item, dest_item)
                         	print("Copied file {} to {}".format(source_item, dest_item))
# Call the function to copy files and directories
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python copy_script.py <source1> <destination1> <source2> <destination2> ...")
        sys.exit(1)

    # The first argument (sys.argv[0]) is the script name, so we skip it.
    args = sys.argv[1:]

    # Separate the sources and destinations
    source_list = args[0::2]  # Elements at even indices
    destination_list = args[1::2]  # Elements at odd indices

    if len(source_list) != len(destination_list):
        print("Error: The number of source and destination paths must match.")
    else:
	f_d_copy(source_list, destination_list)
