# File Open
"""
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)
"""
#   File read
demofiletxt='''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''
f = open("demofile.txt", "r")
print(f.read())
# If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#   File close
f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt", "r") as f:
  print(f.read())
# Then you do not have to worry about closing your files, the statement takes care of that.with

#   Read Only Parts of the File
with open("demofile.txt", "r") as f:
  print(f.read(5)) # Hello

#   Read lines
# You can return one line by using the method:readline()
with open("demofile.txt") as f:
  print(f.readline()) # Hello! Welcome to demofile.txt

# By calling two times, you can read the two first lines:readline()
with open("demofile.txt") as f:
  print(f.readline()) # Hello! Welcome to demofile.txt
  print(f.readline()) # This file is for testing purposes.

# By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)
"""
[1] Hello! Welcome to demofile.txt
[2] This file is for testing purposes.
[3] Good Luck!
"""
