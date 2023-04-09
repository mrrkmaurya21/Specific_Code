import os

folder = r'C:\400k_2352k'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
filenames=os.listdir(folder)
    # Construct old file name
# Iterate over the filenames and rename them
count=6000
for filename in filenames:
    old_name = os.path.join(folder_path, filename)
    new_name = os.path.join(folder_path, str(count)+"wath"+filename )
    os.rename(old_name, new_name) 