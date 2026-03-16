import os
# Create Folder
new_folder_name = 'new_folder'
os.mkdir(new_folder_name)
# mkdir - make directory

# Remove Folder
new_folder_name = 'new_folder'
os.rmdir(new_folder_name) # only deletes empty directories
# rmdir - remove directory

# Checking access rights to a specific file
name = './11.py' # will work the same as '11.py'

print(os.access(name, os.F_OK)) # Existence
print(os.access(name, os.R_OK)) # Readability
print(os.access(name, os.W_OK)) # Writeability
print(os.access(name, os.X_OK)) # Executeability

import time
file_name = 'new.txt'

with open(file_name, 'w') as file:
    file.write('Last words before removal...')
    # in 'x' mode, if file does not exist, it is created
    # otherwise - FileExistsError: [Errno 17] File exists: 'new.txt'

time.sleep(3) # 3-second delay

os.remove(file_name)

'''
'r'  -  read mode
'w'  -  write mode
'a'  -  append mode
'x'  -  create mode
'''
