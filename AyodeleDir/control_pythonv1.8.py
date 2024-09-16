import time
import os
import shutil

source_list = [
    "/u02/jdk/bin",
    "/u02/instantclient",
    "/backup/AWSJULY24/DATAPUMP",
    "/home/Cloudserver/scripts/appfile.txt",
    "/home/Cloudserver/scripts/first_file.txt",
    "/home/Cloudserver/scripts/create_tosyn_dir.sh",
    "/home/Cloudserver/1.txt"
]

destination_list = [
    "/backup/AWSJULY24/Ctaiwo",
    "/backup/AWSJULY24/lawrence",
    "/home/Cloudserver/scripts/bimbbo",
    "/home/Cloudserver/scripts/ayodle",
    "/u01/transient_files/peter",
    "/u01/instantclient/bumii",
    "/home/Cloudserver/scripts/victor"
]

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
                        print("Copied directory {} to {}".format(source_item, dest_time))
                    else:
                        shutil.copy2(source_item, dest_item)
                        print("Copied file {} to {}".format(source_item, dest_time))
# Call the function to copy files and directories
f_d_copy(source_list, destination_list)
