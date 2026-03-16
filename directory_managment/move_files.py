import os

relative_path = '../'        # . means current working directory
absolute_path = os.getcwd() # absolute path to the current working directory

print(absolute_path)
# os.listdir - The "show me what's inside" command
print(os.listdir(relative_path))
print(os.listdir(absolute_path))

# Analyzes a file or folder
path = os.getcwd()
# get cwd - current working directory
for entry in os.listdir('/Users/User/Desktop/NikitaUssyukin/Lectures/G1/Week08/directories_and_files'):
    print('Name:', entry)
    print('Is file:', os.path.isfile(entry))
    print('Is folder:', os.path.isdir(entry))
    print('-----------------')


path = os.getcwd()
# get cwd - current working directory
entries = os.scandir(path) # Creates a "smart" pointer to the folder contents.
print(entries)  # <nt.ScandirIterator object at 0x000001D44E2034F0>
print(type(entries)) # <class 'nt.ScandirIterator'>

for entry in entries:
    print('Name:', entry.name)
    print('Full path:', entry.path)
    print('Is file:', entry.is_file())
    print('Is folder:', entry.is_dir())
    print('Full path (excluding the file):', entry.path.removesuffix(entry.name)) # Cut off the file name from the end
    print('Full path (excluding the file):', entry.path[:-len(entry.name)]) # Cut off so much from the end
    
    print('-----------------')
