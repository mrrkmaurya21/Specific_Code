import os

# Set the path to the folder containing the files
folder_path = r'C:\Users\Admin\OneDrive\Desktop\Ravi_Crunchbase'

# Use the os.listdir() function to get a list of the filenames in the folder
filenames = os.listdir(folder_path)
#print(filenames)
print('number of files:',len(filenames))
c=[]
for i in filenames:
    if len(i)==6:
        c.append(int(i[:1]))
    elif len(i)==7:
        c.append(int(i[:2]))
    elif len(i)==8:
        c.append(int(i[:3]))
    elif len(i)==9:
        c.append(int(i[:4]))
s=sorted(c)
for j in range(1,2354):
    if j not in s:
        print("Missing file number: ", j)
    
def find_duplicates(s):
    return [number for number in set(s) if s.count(number) > 1]

print(find_duplicates(s))
