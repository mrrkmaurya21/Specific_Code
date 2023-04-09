import os

# Set the path to the folder containing the files
folder_path = r'A:\check'

# Use the os.listdir() function to get a list of the filenames in the folder
filenames = os.listdir(folder_path)
#print(filenames)
print(len(filenames))
"""
for filename in filenames:
  # Use the os.rename() function to rename the file
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, 'new_' + filename))"""

# Iterate over the filenames and rename them
"""cc=[]
for i in filenames:
    if len(i)==11:
        cc.append(int(i[:2]))
    if len(i)==12:
        cc.append(int(i[:2]))
    if len(i)==13:
        cc.append(int(i[:3]))
print(cc)"""
count=51
for filename in filenames:
    old_name = os.path.join(folder_path, filename)
    new_name = os.path.join(folder_path,str(count)+'k'+filename[-4:] )
    os.rename(old_name, new_name)
    count+=1