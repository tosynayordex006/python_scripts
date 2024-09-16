import time
import os
import shutil

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
	else:
		print("source path {} does not exist".format(source))
if __name__ == "__main__":
    source_list = []
    destination_list = []
    
    while True:
	source = raw_input("Enter source path (or 'done' to finish): ")
        if source.lower() == 'done':
            break
        destination = raw_input("Enter destination path: ")
        
        source_list.append(source)
        destination_list.append(destination)
    
    if len(source_list) != len(destination_list):
        print("Error: The number of source and destination paths must match.")
    elif len(source_list) == 0:
        print("No source and destination paths provided.")
    else:
        f_d_copy(source_list, destination_list)
